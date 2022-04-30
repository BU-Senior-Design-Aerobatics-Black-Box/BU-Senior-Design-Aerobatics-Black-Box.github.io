# Software Report
## Software Overview:
![](https://github.com/BU-Senior-Design-Aerobatics-Black-Box/BU-Senior-Design-Aerobatics-Black-Box.github.io/blob/main/Software_Overview.PNG)

## Necessary Software Installation
There are several necessary packages that need to be installed.
### Install python and python3: 
`sudo pip3 install python & python3`
### Enable the I2C port:

`sudo raspi-config`

Select Interfacing Options > I2C.

Select Yes when prompted to enable the I2C interface.

Select Yes when prompted to automatically load the I2C kernel module.

Select Finish.

Select Yes when prompted to reboot.

### Enable the Webcam:

`sudo raspi-config`

Select Interfacing Options > web camera.

Select Yes when prompted to enable the web camera interface.

Select Yes when prompted to automatically load the web camera module.

Select Finish.

Select Yes when prompted to reboot.

### Install OpenGL(3.1.6):
#### python3:
`pip3 install PyOpenGL PyOpenGL_accelerate`
#### python2.7:
`pip install PyOpenGL PyOpenGL_accelerate`

### Install Pygame(1.9.4.post1):
#### python3:
`sudo apt-get install python3-pygame`
#### python2.7:
`sudo apt-get install python-pygame `

### Install Guizero(1.3.0):
#### python3:
`sudo pip3 install guizero`
Notice: guizero package currently doesn't support python2.7 or earlier.

### Install RTImuLib(7.2.1):
#### python3:
`sudo pip3 install RTIMULib`
#### python2.7:
`sudo pip install RTIMULib`

### Install smbus(4.1-1):
#### python3:
`sudo apt-get install -y python3-smbus`
#### python2.7:
`sudo apt-get install -y python-smbus`

### Install numpy, matplotlib, OpenCV, sklearn, skimage:
```
pip3 install numpy matplotlib opencv-python scikit-learn scikit-image
```

## Auto running:
Go to terminal and type `sudo nano /etc/xdg/autostart/display.desktop`
In the editor, typing
```
[Desktop Entry]
Name=Display
Exec=/usr/bin/python3 /home/pi/Desktop/Senior_Design_Project/gui2.py
```
