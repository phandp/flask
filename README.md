# PHOTOTAG collaborative project

this project aims to showcase the end-to-end workflow of a Machine Learning application. In the Front End, one can choose an image without any tag which will be analysed in this server app. A list of tags with associated confindence levels are returned to the FE.

This server can run on a local machine or in the cloud, for instance on a AWS EC2 instance. 

team members: Peter HIRT, Shreyas Saxena

# Installation

copy the directory in a folder of choice on your local machine. Make sure that the required prerequisites are available in this folder. See on chapter prerequisites on how to prepare for.

Start the server by : python app.py

Test if the server runs correctly by sending a request to localhost:5000. It should answer with the 
"Machine Learning Server"

to test if the http call is OK, run the below command

curl -i -X POST -H "Content-Type: application/json" -d '{"id":6}' http://localhost:5000/api/ML/photoTag/create

on my iMAC, this app runs outside any environment also.

# Prerequisites

  
  * python version 2.7.9
  * flask version 0.10.1
  * flask-ext.cors version 2.1.0
  * pandas version 0.14.1
  * sklearn version 0.15.2
  * json version 2.0.9
  * logging version 0.5.1.2




# Client Side comments

the project is under the htdocs directory called ild-cnn

the client side is done with in the directory photoTag and running with a Gulp script invoking localhost:3000

start with gulp serve
