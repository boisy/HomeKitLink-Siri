# HomeKitLink Siri 

![https://github.com/Ghawken/HomeKitLink-Siri/blob/master/Images/icon.png](https://github.com/Ghawken/HomeKitLink-Siri/blob/master/Images/icon.png)



Homekit enabler.. 

This plugin aims to allow you to create HomeKit Bridges, which you add your indigo devices to and allows control from within Homekit and Siri control of your setup Apps.


First install

Need Python 3 version of Indigo 2021.2.0
Download latest and greatest indigoplugin file,
Double click to install

Expect to see some immediate error messages as will need to download and install one package:

Either after or before in a terminal window
sudo pip3 install cryptography

Restart the plugin.

Return to the terminal window and copy and paste the below

This removes the apple quarantine bit for downloaded files and is needed for full function.  Very annoyingly unlike the pip3 command it is needed everything you upgrade!
Arghh.. Apple...

sudo xattr -rd com.apple.quarantine /Library/Application\ Support/Perceptive\ Automation/Indigo\ 2022.1/Plugins 
 

Limitations:

Only one indigo device, once, can be published to any HomeKit Bridge.  Seperate indigo devices but one physical device = no problem eg. motion, light sensors.
If you wish the exactly same device eg. 2 dimmer devices to be available in homekit - potentially under different names this is not possible without some simple help.
Simply use Masquerade plugin, or virtual devices and copy the device wished into a new device - use this new device within this plugin.  Repeat as many times as wished.

Everything is user selectable - for example a physical light switch, can be a motion sensor, or occupancy sensor. 
This leads to a bit of setup work, but once device is selected and setup, saved, no need to revisit.

If you break HomeKit by your 'poor' device option - in the normal course of events you simply remove the device from the HomeKit bridge and start again..

This is Beta Software...  

Setup: Next

Create a HomeKit - insert name - Bridge device.
Select the devices you wish to publish,  and select what device it should be, click save

Here the options need explaining:
You can select any device (if Showall selected)
If you are setting up a sensor device - this is a device that returns sensor information to HomeKit - the plugin will give you an option of what deviceState to use.
Often this should be sensorValue - this is the standard value of any sensor.   Sometimes if you are selecting a plugin to be a sensor device 
eg. piBeacon sensors - you will choose the best value.
Importantly for most On/Off Motion/Occupancy Sensors this should be true/False.
Temperature/Humidity number values - need JUST the number value - no degrees C  or degrees F.  Just 22.1
If in doubt check the device in question states to review.  If problematic the plugin will display 0, and/or give an error.

In the aim of keeping the options completely open - you can select anything .... however it does require some inital device setup/thinking.

Lights - dimmer/brightness/Color
Lightbulb:  Should be the choice for all light devices.

Switch:  Within Homekit this can be changed to Switch, Fan, and something else I forget.
This is simply On/off device.
Action Groups default to this option.
Any onOff device within indigo should be supported.

Cameras:
Blue Iris - options come from the Blue Iris plugin, if you haven't installed this and you wish to use Blue Iris - you should.  It enables Motion detection for each camera, live with HomeKit notifications, and Doorbell option exists for each camera.
eg. press Doorbell and get Notification and live stream click access.
Security Spy - camera streams, Doorbell can also be selected.  Motion detection is pending some plugin changes if possible

Motion Sensor:
Temperature Sensor:
Humidity Sensor:
Above rules apply, either defaults to Sensorvalue or can select another state to be used..

