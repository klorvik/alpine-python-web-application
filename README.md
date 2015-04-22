# Flask web application 

## Directory Structure

	/app
		/modules
		/static	
		/templates
	config.py
	run.py
	shell.py

## Setup

	$ virtualenv env
	$ env/bin/pip install flask
	$ env/bin/pip install flask-sqlalchemy
	$ env/bin/pip install flask-wtf

## Running
	Activate environment:
	$ . env/bin/activate
	
	Initialize DB:
	$ python shell.py
		>>> from app import db
		>>> db.create_all()
		>>> exit()
	
	Run:
	$ python run.py
