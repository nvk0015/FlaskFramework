This repository is created to understand the working of flask application framework, and deploy the Machine Learning projects on the web applications. 


Flask is a web applcation framework developed by Armin Ronacher which is written in Python. 

Flask framework is based on WSGI concept, and on Jinja 2 template engine. 

WSGI: Web Server Gateway Interface.
WSSGI is a standard protocol to communicate between the web application and its web server. 

Jinha2: 
It is a web templating system. It basically combines a web template along with a certain data source. It allows to render dynamic pages. 
Some examples for data sources could be Databases, or Machine learning pickle files. 

Building Url dynamically:
The file appDynamicUtl.py shows how url can be dynamically built using variable rules and also how redirecting the web pages work using "redirect" method. 

Integrating HTML with Flask:
The main.py script shows how an existing HTML file can be called

Live streaming:
The python script appVideoStream.py along with CamIndex.html stream a live video with the help of opencv video stream functionality on web pages. 