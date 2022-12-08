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

@app.route("/getAllRamen", methods=["GET","POST"])
def returnAllRamen():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM RAMEN_RATINGS")
        rows = cursor.fetchall()
        # for each in rows:
        #     print(each)

    return jsonify(rows)
if __name__ == "__main__":
    app.run(debug=True)