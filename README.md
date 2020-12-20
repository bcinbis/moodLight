![logo](moodlightLogo.jpg)
Baran Cinbis, Evan Hashemi, Lorand Cheng Hack UMass 2020 
project

## What is Moodlight?
### In a tweet
Words are hard. Saying them to people? EVEN HARDER. Find it hard at social events to ask if someone’s single? To leave you alone? Or do you hate intros like What team or organization are you with? Then use Moodlight! Let Moodlight show others the things you don’t want to say/ask

### Overview
Our project is broken up into two basic parts: event creation and participant joining. The event creator end of the program works through a html web site. Here event creators can send a request to create their event to our server hosted on Google Cloud Platform. If all the data was entered correctly, a successful response is sent back to the event creator and the event is stored into our Google CloudSQL Postgres database. After this, everything on the event creator end is completed.  

The participant end of the project, the Moodlight itself, is where all of the hardware is located. Users complete all of their interactions through an LED matrix and two buttons to work through the setup. When Starting the Moodlight, users use buttons to scroll through letters and choose those corresponding to the code for their gathering. Once that is submitted, the program sends a https request to the server which sends back all of the download links to the images for that given party. These images are downloaded and stored on the RPi. From here, the user simply uses the buttons to scrolls through which image is displayed on their LED screen. They can then hold down either button for 4 seconds to end the program and delete all images from this party


## Installation
### Required Hardware
Here is the hardware that makes up the moodlight
- [Adafruit RGB matrix RPi Bonnet](https://www.adafruit.com/product/3211)
- [Adafruit 32x32 LED Matrix](https://www.adafruit.com/product/2026)
- AC to DC wall plug Power Supply with 5V and at least 4A
- Our 

### Downloads and Settings
Here are the following python libraries that are used and should be downloaded on your RaspberryPi  
- pip install requests
- follow installation instructions [here](https://learn.adafruit.com/adafruit-rgb-matrix-bonnet-for-raspberry-pi/driving-matrices) This contains hardware setup as well for moodlight

Here are the installations to be downloaded onto the server

    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get -y install python3-pip
    sudo pip3 install flask python-dotenv
    sudo apt-get install postgresql-client -y
    sudo apt-get install python3-psycopg2

On your RPi, enter the following into the command line to enable writing/reading of all files:
- sudo chmod -R 777 ~/moodLight


## Software, Server, and Setup of Everything in Between
### Setup Server and Database
How to setup a server and postgreSQL database on Google Cloud Platform
- [Setup a Server](https://linuxhint.com/setup_google_cloud_server/). Run 'moodLight/server/server.py' on the instance you create
- [Setup postgreSQL database](https://www.cloudbooklet.com/setup-cloud-sql-for-postgresql-on-google-cloud/) Connect to the postgres database by filling out the database.ini configuration file on the server

### How to Run RPi Progam
- Navigate to 'moodlight/rpi' directory in a terminal
- Type the following command to begin: sudo python3 main.py
