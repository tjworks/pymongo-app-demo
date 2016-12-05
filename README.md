# MongoDB Fast Development Demo 

## Overview

Build a simple CRUD type of simple web app to manage customer list. 

Demonstrate following MongoDB benefits:

- Dynamic schema: No need to define schema upfront
- Ease of development: 2 lines for insert, 2 lines for getting data out and send back to front end
- Agility: Schema change requires no DB change


## Preparation 

### Install MongoDB

		https://docs.mongodb.com/manual/installation/

### Install PIP if needed

		https://pip.pypa.io/en/stable/installing/

### Install Python modules, including PyMongo driver

		sudo pip install fabric Flask pymongo

### Checkout repo			

		git clone http://github.com/tjworks/pymongo-app-demo


## Demo Steps

#### Browser Demo 

- Run the script: 

 				python app.py

- Open browser to http://localhost:5000
- Demo add/update/delete
- Go to mongodb to review the data in Mongo
	- find()
	- findOne()
	- update()
 				
#### Code review

- Open app.py
- Explain the db connection on top
- Explain addCustomer function:
	- JSON from http request
	- JSON insert into Mongo
	- 2 lines of code

- Explain getCustomer
	- find from DB
	- immediately return
	- No conversion whatsoever needed for JSON 

#### Add a new field

Here we demonstrate when we evolve our program, we are adding a new field to the customer object: "sex"

- Open **templates/list.html**
- Search for "email"
- For every occurrance of "email", add a similar section below email for "sex"
- Save the html file and restart the app.py
- Notice the new field occurring on UI, add a new customer, edit one
- Verify the sex field is in mongodb from mongo shell

The point is that we only needed to change in the code(HTML code!) and didn't have to mess around with the database for the new schema change. 

A screenshot of the change can be viewed here: https://www.dropbox.com/s/m27xrrtdw4ursrv/Screenshot%202016-12-05%2012.59.33.png?dl=0

