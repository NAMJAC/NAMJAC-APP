import mysql.connector
from flask import Flask, jsonify, request

def dbconnect():
    db = mysql.connector.connect(
        host        = "127.0.0.1",  # localhost
        user        = "jgarland",   # Username
        passwd      = "P#pp3r0n!",  # Generic Password
        database    = "prototype"   # Database Schema
        )
    return db


app = Flask(__name__)

# MAKES TABLE
@app.route('/make', methods=['GET','POST', 'DELETE'])
def make():

    # POST to /make
    if request.method == 'POST':
        
        # Fetch json data from request
        data = request.get_json()
        make_name = data['make_name']
        country_of_origin = data['country_of_origin']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # Insert data from request into DB
        cur.execute("INSERT INTO make(make_name, country_of_origin) VALUES(%s, %s)",(make_name, country_of_origin))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 201
        
    # DELETE from /make
    elif request.method == 'DELETE':
    
        # Fetch id number from request
        data = request.get_json()
        make_id = data['make_id']
        
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # find and delete entry with id
        cur.execute("DELETE FROM make WHERE make_id = %s",(make_id,))
        
        # Save & Close DB Connection
        db.commit()
        db.close()
        
        # Update Requester with result
        return 'success', 200
    
    # GET from /make
    else:
    
        # open connection to DB
        db = dbconnect()
        cur = db.cursor()
        
        # get all entries from make
        cur.execute("SELECT * FROM make")
        rows = cur.fetchall()
        
        # close DB connection
        db.close()
        
        # Create a dictionary and populate it
        make_list = []
        make_list.append({'count':len(rows)})
        for i in range(len(rows)):
            make_list.append({'make_id':str(rows[i][0]),'make_name':str(rows[i][1]),'country_of_origin':str(rows[i][2])})
            
        # Send convert dictionary to json and send it to requester
        return jsonify(make_list), 200

    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
