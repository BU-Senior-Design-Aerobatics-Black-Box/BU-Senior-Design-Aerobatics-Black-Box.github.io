import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
import datetime

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

vertices = (
	(2,-0.5,-1),
	(2,0.5,-1),
	(-2,0.5,-1),
	(-2,-0.5,-1),
	(2,-0.5,1),
	(2,0.5,1),
	(-2,-0.5,1),
	(-2,0.5,1)
	)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (1.0, 0.5, 1),
	(0,1,0),
	(0,0,1),
	(5,10,5),
	(1,1,1),
	(0,1,1)
    )

def Cube():
    glBegin(GL_QUADS)
    """
    for surface in surfaces:
        #glColor3f(1.0, 0.5, 1)
    """
    for vertex in surfaces[0]:
        glVertex3fv(vertices[vertex])
        glColor3f(1.0, 0, 0)
    
    for vertex in surfaces[1]:
        glVertex3fv(vertices[vertex])
        glColor3f(1, 0, 1)
    
    for vertex in surfaces[2]:
        glVertex3fv(vertices[vertex])
        glColor3f(0, 0, 1)
        
    for vertex in surfaces[3]:
        glVertex3fv(vertices[vertex])
        glColor3f(1.0, 1, 0)
        
    for vertex in surfaces[4]:
        glVertex3fv(vertices[vertex])
        glColor3f(1.0, 1, 1)
    
    for vertex in surfaces[5]:
        glVertex3fv(vertices[vertex])
        glColor3f(1.0, 0.5, 1)
    glEnd()
    
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glTranslatef(0.0, 0.0, -7.0)

def Draw(roll,pitch,yaw):
    glRotatef(pitch,0.1,0,0) #(deg, pitch, yaw, roll)
    glRotatef(yaw,0,0.1,0)
    glRotatef(roll,0,0,0.1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()

pitch_prev = 0
yaw_prev = 0
roll_prev = 0

a = datetime.datetime.now()
time_prev = a
file1 = open("/home/pi/Desktop/Senior_Design_Project/IMU_data.txt", "a")
file1.write('Start Time: %s\n' %(a))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    if imu.IMURead():
    # x, y, z = imu.getFusionData()
    # print("%f %f %f" % (x,y,z))
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
        current_time = datetime.datetime.now()
        running_time = current_time - time_prev
        file1.write('Running Time = %s Roll = %f Pitch = %f Yaw =%f\n' %(running_time, fusionPose[0], fusionPose[1], fusionPose[2]))
        file1.flush()
        pitch = math.degrees(fusionPose[1]) - pitch_prev
        yaw = math.degrees(fusionPose[2]) - yaw_prev
        roll = math.degrees(fusionPose[0]) - roll_prev
        """
        pitch = 1.654395
        yaw = -73.218931
        roll = 7.650929
        """
        print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
            math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
        Draw(roll, pitch, yaw)
        pitch_prev = math.degrees(fusionPose[1])
        yaw_prev = math.degrees(fusionPose[2])
        roll_prev = math.degrees(fusionPose[0])
        #time.sleep(poll_interval*1.0/1000.0)
file1.close()

    
    