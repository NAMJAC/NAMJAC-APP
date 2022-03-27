#__________                __         ___________           .___
#\______   \_____    ____ |  | __     \_   _____/ ____    __| _/
# |    |  _/\__  \ _/ ___\|  |/ /      |    __)_ /    \  / __ | 
# |    |   \ / __ \\  \___|    <       |        \   |  \/ /_/ | 
# |______  /(____  /\___  >__|_ \_____/_______  /___|  /\____ | 
#        \/      \/     \/     \/_____/       \/     \/      \/ 

# Created by Jackson Garland for NAMJAC Development
# 3/26/2022

import mysql.connector
from flask import Flask, jsonify, request

def dbconnect():
    db = mysql.connector.connect(
        host        = "127.0.0.1",  # localhost
        user        = "flask",      # Username
        passwd      = "1533928",    # Generic Password
        database    = "api"         # Database Schema
        )
    return db


app = Flask(__name__)

#_________                 __                               
#\_   ___ \ __ __  _______/  |_  ____   _____   ___________ 
#/    \  \/|  |  \/  ___/\   __\/  _ \ /     \_/ __ \_  __ \
#\     \___|  |  /\___ \  |  | (  <_> )  Y Y  \  ___/|  | \/
# \______  /____//____  > |__|  \____/|__|_|  /\___  >__|   
#        \/           \/                    \/     \/       

@app.route('/customer', methods=['GET','POST', 'DELETE'])
def customer():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        Cust_ID = data['Cust_ID']
        Contact_Type_ID = data['Contact_Type_ID']
        First_Name = data['First_Name']
        Last_Name = data['Last_Name']
        Address = data['Address']
        City = data['City']
        State = data['State']
        zipcode = data['zipcode']
        Phone_number = data['Phone_number']
        Email = data['Email']
        active = True
        
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Customer(Cust_ID, Contact_Type_ID, First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(Cust_ID, Contact_Type_ID, First_Name, Last_Name, Address, City, State, zipcode, Phone_number, Email, active))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
        
    # Logical Delete
    elif request.method == 'DELETE':
    
        # Fetch id number from request
        data = request.get_json()
        Cust_ID = data['Cust_ID']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # find and delete entry with id
        cur.execute("UPDATE Customer SET active = false WHERE Cust_ID = %s",(Cust_ID,))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
    
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
            'Contact_Type_ID':  str(rows[i][1]),
            'First_Name':       str(rows[i][2]),
            'Last_Name':        str(rows[i][3]),
            'Address':          str(rows[i][4]),
            'City':             str(rows[i][5]),
            'State':            str(rows[i][6]),
            'zipcode':          str(rows[i][7]),
            'Phone_number':     str(rows[i][8]),
            'Email':            str(rows[i][9])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Customer_list), 200


#  _________                  .__              
# /   _____/ ______________  _|__| ____  ____  
# \_____  \_/ __ \_  __ \  \/ /  |/ ___\/ __ \ 
# /        \  ___/|  | \/\   /|  \  \__\  ___/ 
#/_______  /\___  >__|    \_/ |__|\___  >___  >
#        \/     \/                    \/    \/ 

@app.route('/service', methods=['GET','POST', 'DELETE'])
def service():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        Service_ID = data['Service_ID']
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
        cur.execute("INSERT INTO Service(Service_ID, Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(Service_ID, Cust_ID, service_name, service_amount, service_description, service_date_init, service_date_completed, active))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
        
    # Logical Delete
    elif request.method == 'DELETE':
    
        # Fetch id number from request
        data = request.get_json()
        Service_ID = data['Service_ID']
        
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
    
    # fetch
    else:
    
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Service
        cur.execute("SELECT * FROM Service WHERE active = true")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Customer_list = []
        Customer_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Customer_list.append({
            'Service_ID':          		str(rows[i][0]),
            'Cust_ID':  				str(rows[i][1]),
            'service_name':       		str(rows[i][2]),
            'service_amount':       	str(rows[i][3]),
            'service_description':      str(rows[i][4]),
            'service_date_init':        str(rows[i][5]),
            'service_date_completed':	str(rows[i][6])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Customer_list), 200


#_________                __                 __   ___________                        __________                 _____                                         
#\_   ___ \  ____   _____/  |______    _____/  |_ \__    ___/__.__.______   ____     \______   \_______   _____/ ____\___________   ____   ____   ____  ____  
#/    \  \/ /  _ \ /    \   __\__  \ _/ ___\   __\  |    | <   |  |\____ \_/ __ \     |     ___/\_  __ \_/ __ \   __\/ __ \_  __ \_/ __ \ /    \_/ ___\/ __ \ 
#\     \___(  <_> )   |  \  |  / __ \\  \___|  |    |    |  \___  ||  |_> >  ___/     |    |     |  | \/\  ___/|  | \  ___/|  | \/\  ___/|   |  \  \__\  ___/ 
# \______  /\____/|___|  /__| (____  /\___  >__|____|____|  / ____||   __/ \___  >____|____|     |__|    \___  >__|  \___  >__|    \___  >___|  /\___  >___  >
#        \/            \/          \/     \/  /_____/       \/     |__|        \/_____/                      \/          \/            \/     \/     \/    \/ 

@app.route('/contact_type_preference', methods=['GET','POST', 'DELETE'])
def contact_type_preference():

    # Create entry
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        Contact_Type_ID = data['Contact_Type_ID']
        Cust_ID = data['Cust_ID']
        Phone_number = data['Phone_number']
        Email = data['Email']
        active = True
        
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO Contact_Type_Preference(Contact_Type_ID, Cust_ID, Phone_number, Email, active) VALUES(%s, %s, %s, %s, %s)",(Contact_Type_ID, Cust_ID, Phone_number, Email, active))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
        
    # Logical Delete
    elif request.method == 'DELETE':
    
        # Fetch id number from request
        data = request.get_json()
        Contact_Type_ID = data['Contact_Type_ID']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # find and delete entry with id
        cur.execute("UPDATE Contact_Type_Preference SET active = false WHERE Contact_Type_ID = %s",(Contact_Type_ID,))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
    
    # fetch
    else:
    
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from Contact_Type_Preference
        cur.execute("SELECT * FROM Contact_Type_Preference WHERE active = true")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        Customer_list = []
        Customer_list.append({'count':len(rows)})
        for i in range(len(rows)):
            Customer_list.append({
            'Contact_Type_ID':          		str(rows[i][0]),
            'Cust_ID':  				str(rows[i][1]),
            'Phone_number':       		str(rows[i][2]),
            'Email':       	str(rows[i][3])
            })
            
        # Send convert dictionary to json and send it to requester
        return jsonify(Customer_list), 200
 
if __name__ == '__main__':
    app.run(host="0.0.0.0")
