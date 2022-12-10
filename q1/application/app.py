from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db_files/ramen-ratings.sqlite")
        print(conn)
    except sqlite3.error as e:
        print(e)
        print("db conn error")
    return conn

## Retrieve All Rows in DB
@app.route("/getAllRamen")
def returnAllRamen():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM RAMEN_RATINGS")
        rows = cursor.fetchall()
        # for each in rows:
        #     print(each)

    return jsonify(rows)

## Create Ramen Review
# @app.route('/createReview', methods=("GET",'POST'))
@app.post('/createReview')
def createReview():
    if request.method == 'POST':

        content = request.get_json()
        print(content)

        id = content['ID']
        country = content['Country']
        brand = content['Brand']
        type = content['Type']
        package = content['Package']
        rating = content['Rating']

  
        # id = request.form['ID']
        # country = request.form['Country']
        # brand = request.form['Brand']
        # type = request.form['Type']
        # package = request.form['Package']
        # rating = request.form['Rating']


        if isinstance(rating, (int, float)) != True:
            print(isinstance(rating, (int, float)))
            print("rating: ", rating)
            return "Rating has to be number"

        conn = db_connection()
        conn.execute('INSERT INTO RAMEN_RATINGS (id, country, brand, type, package, rating) VALUES (?, ?, ?, ?, ?, ?)',
                        (id, country, brand, type, package, rating))
        conn.commit()
        conn.close()
        return jsonify({"result" : "Success", "content":"new ramen is added"})

@app.post('/modifyReview')
def modifyReview():

    ## Does Not Exist then....
    ## Else just modify
    ## check if not null? 
    if request.method == 'POST':

        content = request.get_json()

        id = content['ID']
        country = content['Country']
        brand = content['Brand']
        type = content['Type']
        package = content['Package']
        rating = content['Rating']


        # if isinstance(rating, (int, float)) != True:
        #     print(isinstance(rating, (int, float)))
        #     print("rating: ", rating)
        #     return "Rating has to be number"

        conn = db_connection()

        cursor = conn.execute('SELECT * FROM RAMEN_RATINGS WHERE id = ? and country = ? and brand = ? and type = ? and package = ? and rating = ?',(id, country, brand, type, package, rating))
        rows = cursor.fetchall()
        print("Rows:", rows)
        if len(rows) == 0:
            return jsonify({"result" : "Error", "content":"no rows exist"})
        elif len(rows) > 1:
            return jsonify({"result" : "Error", "content":"Duplicated rows exist, please check db / contact support"})


        ## check if to update values already exist
        new_id = content['new_ID']
        new_country = content['new_Country']
        new_brand = content['new_Brand']
        new_type = content['new_Type']
        new_package = content['new_Package']
        new_rating = content['new_Rating']
       
        cursor = conn.execute('SELECT * FROM RAMEN_RATINGS WHERE id = ? and country = ? and brand = ? and type = ? and package = ? and rating = ?',(new_id, new_country, new_brand, new_type, new_package, new_rating))
        rows = cursor.fetchall()
        if len(rows) > 0:
            return jsonify({"result" : "Error", "content":"An existing row already exist with the updated values, please check db / contact support"})

        
        ## update row if no errors found
        print("old_id:", id)
        print("new_id:", new_id)
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute('''UPDATE RAMEN_RATINGS SET id = ? and country = ? and brand = ? and type = ? and package = ? and rating = ?
                          WHERE id = ? and country = ? and brand = ? and type = ? and package = ? and rating = ?''',
                         (new_id, new_country, new_brand, new_type, new_package, new_rating, id, country, brand, type, package, rating))
        conn.commit()
        conn.close()


        # conn.commit()
        # conn.close()
        return jsonify({"result" : "Success", "content":"ramen updated successfully"})

if __name__ == "__main__":
    app.run(debug=True)