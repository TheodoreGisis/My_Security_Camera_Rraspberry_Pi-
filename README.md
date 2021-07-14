# My_Security_Camera_Rasberry_pi
Requirements:

-Rasberry pi zero W


-Rasberry pi Camera

-Rasberry pi zero Case holder

-Micro SD Card (at least 8GB)

-Power Supply

Not necessary:

-Micro HDMI

First of all you need to install your software in your Rasberry.To do that you need to insert your Micro Sd card in to your computer and visit the official 
website of Rasberry: "https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit". Here you can find the software that you want.

If you want to connect your raspberry with your wifi and you are using the lite version just visit this site---->"https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html",
otherwise just plug in your HDMI and use your mouse and your keyboard(you can use HDMI and keyboard only if you installed the deskotop version).

For OpenCV installation in your raspberry just follow the instruction of this site --->"https://learnopencv.com/install-opencv-4-on-raspberry-pi/"

To connect with my Rasberry pi i am using Putty.Find out your locan rasberry pi address and connect using putty.To login in username use "pi" and password "rasberry"

After that connect your Rasberry camera and type "sudo raspi-config".In this blue interface just go to "camera" and press enable.Next step is to reboot your rasberry and then check if the camera is ready to use py typing "raspistill -o Desktop/image.jpg".With this command you have taken a photo and you have store it in the desktop.Using you command lines go to desktop and check if the image is there,if not repeat the step.
