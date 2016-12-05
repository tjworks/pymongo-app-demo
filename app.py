from pymongo import MongoClient
from flask import Flask,render_template,jsonify,json,request
from fabric.api import *
from bson.json_util import dumps

application = Flask(__name__)

client = MongoClient('mongodb:27017')
db = client.mydb1

@application.route("/addCustomer",methods=['POST'])
def addCustomer():
    try:
        json_data = request.json['info']
        # json_data:  { name: "", address: "", email:"", phone: "" }
        db.customers.insert(json_data);        
        return jsonify(status='OK',message='inserted successfully')
    except Exception,e:
        return jsonify(status='ERROR',message=str(e))

@application.route('/')
def showCustomerList():
    return render_template('list.html')

@application.route('/getCustomer',methods=['POST'])
def getCustomer():
    try:
        CustomerId = request.json['customer_id']
        Customer = db.customers.find_one({'customer_id': CustomerId})        
        return dumps(Customer)
    except Exception, e:
        print(e)
        return str(e)

@application.route('/updateCustomer',methods=['POST'])
def updateCustomer():
    try:
        CustomerInfo = request.json['info']
        customer_id = CustomerInfo['customer_id']
        del CustomerInfo["_id"]
        db.customers.update({'customer_id': customer_id},{'$set': CustomerInfo})        
        return jsonify(status='OK',message='updated successfully')
    except Exception, e:
        print(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/getCustomerList",methods=['POST'])
def getCustomerList():
    try:
        customers = db.customers.find();

        CustomerList = []
        for Customer in customers:         
            CustomerList.append(Customer)
    except Exception,e:
        print(e)
        return str(e)
    
    return dumps(CustomerList)

@application.route("/deleteCustomer",methods=['POST'])
def deleteCustomer():
    try:
        CustomerId = request.json['customer_id']
        db.customers.remove({'customer_id': CustomerId })
        return jsonify(status='OK',message='deletion successful')
    except Exception, e:
        return jsonify(status='ERROR',message=str(e))

if __name__ == "__main__":
    application.run(host='0.0.0.0')

