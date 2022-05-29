# MS-Face-Recognition-Project
 A security system for the visually challenged people using Microsoft Azure FaceAPI
Pre-requisite for Client

Node.js version :v16.14.2 to be installed
Npm Version : 8.5.0

Pre-requisite for Server
Python version : 3.9.7 to be installed 

After downloading the project from GitHub, change to the client folder in VSCode inside the project and install the following packages

npm install (installs all packages mentioned in package.json file)
npm install axios
npm install react-webcam

After installing all the above, to start the client application, give command

npm start 

Sever Application

In another terminal window,
Change to flask-server directory

pip install flask
pip install flask-cors
pip install pillow
pip install mysql-connector-python
pip install twilio
pip install azure-cognitiveservices-vision-face

 
After installing all the above, to start the server application, give command

python server.py


Recommended Browsers : 
In MacOS - Safari
Windows/Linux - Chrome

Twilio Setup - to configure the number to which  WhatsApp messages are to be sent

Within the flask-server directory inside the project, open authentication.json.

There are 2 json values. 
Fromwhatsappnumber and towhatsappnumber.

1. Change towhatsappnumber to the desired mobile number to which WhatsApp messages are to be sent. (marked as XXXXXXXXXX)

2. From this number ( new number added in the towhatsappnumber )send this message to the Fromwhatsappnumber - join dust-slabs

To start the server application,
Python server.py

NOTE:
Voice commands for controlling the switch on the Home page:
       1. Alex i am home : to let the appliacation know that you're home
       2. Alex i am going out : to let the appliacation know that you're going out

