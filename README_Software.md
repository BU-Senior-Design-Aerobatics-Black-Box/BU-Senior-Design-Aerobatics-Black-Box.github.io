# Software Report
## Software Overview:


There are several necessary packages that need to be installed.

Install python and python3: `sudo pip3 install python & python3`

## Enable the I2C port:

`sudo raspi-config`

Select Interfacing Options > I2C.

Select Yes when prompted to enable the I2C interface.

Select Yes when prompted to automatically load the I2C kernel module.

Select Finish.

Select Yes when prompted to reboot.

## Enable the Webcam:

`sudo raspi-config`

Select Interfacing Options > web camera.

Select Yes when prompted to enable the web camera interface.

Select Yes when prompted to automatically load the web camera module.

Select Finish.

Select Yes when prompted to reboot.

## Install OpenGL(3.1.6):
### python3:
`pip3 install PyOpenGL PyOpenGL_accelerate`
### python2.7:
`pip install PyOpenGL PyOpenGL_accelerate`

## Install Pygame(1.9.4.post1):
### python3:
`sudo apt-get install python3-pygame`
### python2.7:
`sudo apt-get install python-pygame `
