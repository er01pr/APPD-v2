from flask import Flask, flash, redirect, render_template, request, session, url_for
import sqlite3
import os

#Current Directory of the project
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

#Homepage
@app.route("/")
def home():
    
    #Configure App to connect with the SQLite Database
    connection = sqlite3.connect('appd.db')
    cursor = connection.cursor()
    
    #Read and fetch the Author_name in the database
    readdb = "SELECT AUTHOR_name FROM Author"
    authors = cursor.execute(readdb)
    authors = authors.fetchall()

    #Convert author tuples to list via list comprehension
    author_list = [author[0] for author in authors]
    print(author_list)

    
    return render_template("index.html", author_list=author_list)