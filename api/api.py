
#__________                __         ___________           .___
#\______   \_____    ____ |  | __     \_   _____/ ____    __| _/
# |    |  _/\__  \ _/ ___\|  |/ /      |    __)_ /    \  / __ | 
# |    |   \ / __ \\  \___|    <       |        \   |  \/ /_/ | 
# |______  /(____  /\___  >__|_ \_____/_______  /___|  /\____ | 
#        \/      \/     \/     \/_____/       \/     \/      \/ 

# NAMJAC Development
# 3/26/2022

import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS

def dbconnect():
    db = mysql.connector.connect(
        host        = "127.0.0.1",  # localhost
        user        = "flask",      # Username
        passwd      = "1533928",    # Generic Password
        database    = "api"         # Database Schema
        )
    return db


app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return "Connection Successful", 200


#_________                 __                               
#\_   ___ \ __ __  _______/  |_  ____   _____   ___________ 
#/    \  \/|  |  \/  ___/\   __\/  _ \ /     \_/ __ \_  __ \
#\     \___|  |  /\___ \  |  | (  <_> )  Y Y  \  ___/|  | \/
# \______  /____//____  > |__|  \____/|__|_|  /\___  >__|   
#        \/           \/                    \/     \/       

@app.route('/customer', methods=['GET','POST'])
def customer():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        First_Name = data['First_Name']
        Last_Name = data['Last_Name']
        Address = data['Address']
        City = data['City']
        State = data['State']
        zipcode = data['zipcode']
        Phone_number = data['Phone_number']
        Email = data['Email']
        conpref = data['conpref']
        creation_date = data['creation_date']
        active = True
        
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Customer(First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, conpref, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, conpref, active))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
    
    # fetch
    else:
    
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Customer
        cur.execute("SELECT * FROM Customer WHERE active = true")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Customer_list = []
        Customer_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Customer_list.append({
                'Cust_ID':          str(rows[i][0]),
                'First_Name':       str(rows[i][1]),
                'Last_Name':        str(rows[i][2]),
                'Address':          str(rows[i][3]),
                'City':             str(rows[i][4]),
                'State':            str(rows[i][5]),
                'zipcode':          str(rows[i][6]),
                'Phone_number':     str(rows[i][7]),
                'Email':            str(rows[i][8]),
                'conpref':          str(rows[i][9]),
                'creation_date':    str(rows[i][10])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Customer_list), 200

@app.route('/customer/<int:id>',methods=['GET', 'DELETE','PUT'])
def specific_Customer(id):

    if request.method == 'DELETE':
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # find and delete entry with id
        cur.execute("UPDATE Customer SET active = false WHERE Cust_ID = %s",(id,))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
        
    # Update
    elif request.method == 'PUT':
        
        # Easiest way to do this is to delete and then re-add with the same Cust_ID.
        
        # Fetch json data from request
        data = request.get_json()
        First_Name = data['First_Name']
        Last_Name = data['Last_Name']
        Address = data['Address']
        City = data['City']
        State = data['State']
        zipcode = data['zipcode']
        Phone_number = data['Phone_number']
        Email = data['Email']
        conpref = data['conpref']
        creation_date = data['creation_date']
        active = True
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Delete the old record
        cur.execute("DELETE FROM Customer WHERE Cust_ID = %s",(id,))
        
        # Replace it with new recprd
        cur.execute("INSERT INTO Customer(Cust_ID, First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, conpref, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(id, First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, conpref, active))
   
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
        
    else:
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
    
        # get the entry from Customer with the given id
        cur.execute("SELECT * FROM Customer WHERE active = true AND Cust_ID = %s",(id,))
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Customer_list = []
        for i in range(len(rows)):
            Customer_list.append({
                'Cust_ID':          str(rows[i][0]),
                'First_Name':       str(rows[i][1]),
                'Last_Name':        str(rows[i][2]),
                'Address':          str(rows[i][3]),
                'City':             str(rows[i][4]),
                'State':            str(rows[i][5]),
                'zipcode':          str(rows[i][6]),
                'Phone_number':     str(rows[i][7]),
                'Email':            str(rows[i][8]),
                'conpref':          str(rows[i][9]),
                'creation_date':    str(rows[i][10])
            })

        # Send convert dictionary to json and send it to requester
        return jsonify(Customer_list), 200

@app.route('/pastmonth/customers', methods=['GET'])
def pastcust():

    # open connection to DB
    db = dbconnect()
    cur = db.cursor()
    
    # fetch customers in past month
    cur.execute("SELECT COUNT(Cust_ID) as NUMCUST FROM Customer WHERE creation_date > NOW() - INTERVAL 30 DAY")
    rows = cur.fetchall()
    
    # close DB connection
    db.close()
    
    Customer_list = []
    Customer_list.append({'NewCust': str(rows[0][0]),})
    
    return jsonify(Customer_list), 200
    
    
    
    

#  _________                  .__              
# /   _____/ ______________  _|__| ____  ____  
# \_____  \_/ __ \_  __ \  \/ /  |/ ___\/ __ \ 
# /        \  ___/|  | \/\   /|  \  \__\  ___/ 
#/_______  /\___  >__|    \_/ |__|\___  >___  >
#        \/     \/                    \/    \/ 

@app.route('/service', methods=['GET','POST'])
def service():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        Cust_ID = data['Cust_ID']
        service_name = data['service_name']
        service_amount = data['service_amount']
        service_description = data['service_description']
        service_date_init = data['service_date_init']
        service_date_completed = data['service_date_completed']
        active = True
        
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Service(Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active) VALUES(%s, %s, %s, %s, %s, %s, %s)",(Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
    
    # fetch
    else:
    
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Service
        cur.execute("SELECT * FROM Service WHERE active = true ORDER BY Service_ID DESC")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Service_list = []
        Service_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Service_list.append({
				'Service_ID':          	    str(rows[i][0]),
				'Cust_ID':  		        str(rows[i][1]),
				'service_name':       	    str(rows[i][2]),
				'service_amount':       	str(rows[i][3]),
				'service_description':      str(rows[i][4]),
				'service_date_init':        str(rows[i][5]),
				'service_date_completed':	str(rows[i][6])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Service_list), 200

@app.route('/service/<int:id>',methods=['GET', 'DELETE','PUT'])
def specific_Service(id):

    if request.method == 'DELETE':
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # find and delete entry with id
        cur.execute("UPDATE Service SET active = false WHERE Service_ID = %s",(Service_ID,))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
        
    # Update
    elif request.method == 'PUT':
        
        # Easiest way to do this is to delete and then re-add with the same Cust_ID.
        
        # Fetch json data from request
        data = request.get_json()
        Cust_ID = data['Cust_ID']
        service_name = data['service_name']
        service_amount = data['service_amount']
        service_description = data['service_description']
        service_date_init = data['service_date_init']
        service_date_completed = data['service_date_completed']
        active = True
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Delete the old record
        cur.execute("DELETE FROM Service WHERE Service_ID = %s",(id,))
        
        # Replace it with new recprd
        cur.execute("INSERT INTO Service(Service_ID, Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(id, Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active))
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
        
    else:
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
    
        # get the entry from Service with the given id
        cur.execute("SELECT * FROM Service WHERE active = true AND Service_ID = %s",(id,))
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Service_list = []
        for i in range(len(rows)):
            Service_list.append({
				'Service_ID':          	    str(rows[i][0]),
				'Cust_ID':  		        str(rows[i][1]),
				'service_name':       	    str(rows[i][2]),
				'service_amount':       	str(rows[i][3]),
				'service_description':      str(rows[i][4]),
				'service_date_init':        str(rows[i][5]),
				'service_date_completed':	str(rows[i][6])
            })
			
        # Send convert dictionary to json and send it to requester
        return jsonify(Service_list), 200
   
@app.route('/pastmonth/services', methods=['GET'])
def pastserv():

    # open connection to DB
    db = dbconnect()
    cur = db.cursor()
    
    # fetch customers in past month
    cur.execute("SELECT COUNT(Service_ID) as NUMSERVICE FROM Service WHERE service_date_completed > NOW() - INTERVAL 30 DAY;")
    rows = cur.fetchall()
    
    # close DB connection
    db.close()
    
    Service_List = []
    Service_List.append({'NewServ': str(rows[0][0]),})
    
    return jsonify(Service_List), 200   

#_________                                           
#\_   ___ \  ____  __ ________   ____   ____   ______
#/    \  \/ /  _ \|  |  \____ \ /  _ \ /    \ /  ___/
#\     \___(  <_> )  |  /  |_> >  <_> )   |  \\___ \ 
# \______  /\____/|____/|   __/ \____/|___|  /____  >
#        \/             |__|               \/     \/ 

@app.route('/coupon', methods=['GET','POST'])
def coupon():
    
    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        recipient = data['recipient']
        message = data['message']
        date = data['date']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Coupons(recipient, message, date) VALUES(%s, %s, %s)",(recipient, message, date))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
    
    # fetch
    else:
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Coupons
        cur.execute("SELECT * FROM Coupons ORDER BY Coupon_ID DESC")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        
        Coupon_list = []
        Coupon_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Coupon_list.append({
				'Coupon_ID':    str(rows[i][0]),
				'recipient':  	str(rows[i][1]),
				'message':      str(rows[i][2]),
				'date':         str(rows[i][3])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Coupon_list), 200

#__________                             __          
#\______   \ ____ ______   ____________/  |_  ______
# |       _// __ \\____ \ /  _ \_  __ \   __\/  ___/
# |    |   \  ___/|  |_> >  <_> )  | \/|  |  \___ \ 
# |____|_  /\___  >   __/ \____/|__|   |__| /____  >
#        \/     \/|__|                           \/ 

@app.route('/reports', methods=['GET','POST'])
def reports():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        Customers = data['Customers']
        Services = data['Services']
        avgSPC = data['avgSPC']
        NewCust = data['NewCust']
        NewServ = data['NewServ']
        Coupons = data['Coupons']
        date = data['date']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Reports(Customers, Services, avgSPC, NewCust, NewServ, Coupons, date) VALUES(%s, %s, %s, %s, %s, %s, %s)",(Customers, Services, avgSPC, NewCust, NewServ, Coupons, date))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
    
    # fetch
    else:
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Coupons
        cur.execute("SELECT * FROM Reports ORDER BY Report_ID DESC")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Report_list = []
        Report_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Report_list.append({
				'Report_ID':    str(rows[i][0]),
				'Customers':  	str(rows[i][1]),
				'Services':     str(rows[i][2]),
				'avgSPC':       str(rows[i][3]),
                'NewCust':      str(rows[i][4]),
                'NewServ':      str(rows[i][5]),
                'Coupons':      str(rows[i][6]),
                'date':         str(rows[i][7])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Report_list), 200


if __name__ == '__main__':
    app.run(host='172.26.54.26')
