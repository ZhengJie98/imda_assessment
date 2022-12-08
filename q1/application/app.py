from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("ramen-rating.sqlite")
    except sqlite3.error as e:
        print(e)
        return conn