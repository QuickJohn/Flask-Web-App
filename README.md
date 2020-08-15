# Flask-Web-App

Flask Project

Objectives:
Demonstrate proficiency in the implimentation of Flask, Python, and SQL by  
creating blog site which displays blog entries posted by its registrants.  The registrants must 
create an account with the data stored in a MySQL database which is able to manipulated from a 
Python app.  


Create virtual environment(Windows)

  $ py -3 -m venv <virtual_environment_name>


Export all requirements from virtual env

      $ pip freeze --local > requirements.txt


Delet virtual environment

  $ rm -rf <environment_name>  < linux command


Load requirements

  $ pip install -r <requirements.txt>


Set envoronment variable(Windows PS)$  env:FLASK_APP = "flask_blog.py"

(Linux)$ export FLASK_APP=flask_blog.py

(Windows cmd.exe)$  set FLASK_APP=flask_app.py

IMPORTANT: Environment variable must be set with every new shell/terminal

Debug Mode$  $env:FLASK_DEBUG = 1

Runs application directly through Python by adding following conditional in app

	if __name__ == '__main__':

    	  app.run(debug=True)

Allows for server to be run with {  $ python flask_blog.py  } command, without creating environment variables

