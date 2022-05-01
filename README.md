# Aerobatic Black Box 

![](User%20Manual/logo.png)

 During aerobatic competition the aircraft's flight status, altitude, speed, direction, and overload parameters change drastically. The pilot must be aware of the flight status at any time, understand the changes in motion parameters, and control the aircraft to move on a predetermined trajectory in a timely and accurate manner. During competition and training, AHRS will help pilots understand the real-time aircraft attitude, however this device cannot record and replay 3 demonstrations of flight training, and pilots cannot make precise movement adjustments based on ordinary avionics.
 
 Under this premise, the client put forward the following requirements to us:
1. the equipment must be able to record flight data (including altitude, GPS, and flight attitude). 
2. the equipment must be able to record the pilot's input to the aircraft. 
3. the equipment must be able to replay 3D flight simulations to help pilots adjust flight movements. 
4. flight simulation must be able to switch perspectives to help pilots observe aerobatics.
 
Our Aerobatic Black Box will address client’s issues by providing a hardware part which contains AHRS, INS, and cameras to collect pilot input, and a software part which allows pilots to replay 3D demonstration of flight maneuvers, and also provides pilot input corresponding to every maneuver. When collecting pilot input, we are faced with the problem that the aircraft does not have a collection interface, so we innovatively use image recognition technology to collect airspeed and pilot input.
The Aerobatic Black Box is specially designed for introductory aerobatics pilots and aerobatics training. This system will allow pilots to observe different angles of flight attitude for the next flight adjustment, and also solves the lack of digital AHRS in some aircraft, and greatly reduces the difficulty of aerobatics training.

## System Overview
### Overview Block Diagrams
Hardware Block Diagram:

![](User%20Manual/Hardware%20Block%20Diagram.png)

[Hardware Details](README_Hardware.md)

Software Block Diagram:

![](User%20Manual/Software%20Block%20Diagram.png)

[Software Details](README_Software.md)

User Interface:

![](User%20Manual/User%20Interface.jpg)

## Current State
 IMU: Successfully collect the Roll/Pitch/Yaw data from MPU9250 and using those data to generate a real-time 3D model.
 
 GPS: Successfully collect the longitute/latitute/altitute from NEO-M9N.
 
 Camera: Successfuly using camera to carpture and display the dial reading and the real-time position of the flightstick.
 
 UI: Containing the basic function of the user interface.

## Future Work
IMU: Although we have implemented the Kalman filter to smooth the output data, the final 3D model is still noisy. We will try other possible filter such as complementary filter to erase the noise.

UI: Adding more graphical features to the UI.

Data transfering: Transfering the original data to the .fdr format and displaying them in Xplane11 simulator.

For more info, please look up the [User Manual](https://github.com/BU-Senior-Design-Aerobatics-Black-Box/BU-Senior-Design-Aerobatics-Black-Box.github.io/blob/main/User%20Manual/Final%20User%20Manual.docx)
