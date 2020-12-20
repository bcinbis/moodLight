# moodLight
Baran Cinbis, Evan Hashemi, Lorand Cheng Hack UMass 2020 
project

![logo](moodlightLogo.jpg)

## What is Moodlight?
### In a tweet
Words are hard. Saying them to people? EVEN HARDER. How can you ask someone if they’re single? Or to leave you alone? Use Moodlight! Use Moodlight to display what you’re feeling via pictures to avoid painful convos! Also personalize Moodlight to show team names or custom pics

### Overview
Our project is broken up into two basic parts: event creation and participant joining. The event creator end of the program works through a html web site. Here event creators can send a request to create their event to our server hosted on Google Cloud Platform. If all the data was entered correctly, a successful response is sent back to the event creator and the event is stored into our Google CloudSQL Postgres database. After this, everything on the event creator end is completed.  

The participant end of the project, the Moodlight itself, is where all of the hardware is located. Users complete all of their interactions through an LED matrix and two buttons to work through the setup. When Starting the Moodlight, users use buttons to scroll through letters and choose those corresponding to the code for their gathering. Once that is submitted, the program sends a https request to the server which sends back all of the download links to the images for that given party. These images are downloaded and stored on the RPi. From here, the user simply uses the buttons to scrolls through which image is displayed on their LED screen. They can then hold down either button for 4 seconds to end the program and delete all images from this party


## Installation
### Required Hardware
Here is the hardware that makes up the moodlight
- [Adafruit RGB matrix RPi Bonnet](https://www.adafruit.com/product/3211)
- [Adafruit 32x32 LED Matrix](https://www.adafruit.com/product/2026)
- AC to DC wall plug Power Supply with 5V and at least 4A

### Downloads and Settings
Here are the following python libraries that are used and should be downloaded on your RaspberryPi  
- pip install requests
- follow installation instructions [here](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices) This contains hardware setup as well for moodlight

Here are the following python libraries that are used and should be downloaded wherever you host your server  
- pip install psycopg2
- pip install flask

On your RPi, enter the following into the command line to enable writing/reading of all files:
- sudo chmod -R 777 ~/moodLight

### Setup Server and Database