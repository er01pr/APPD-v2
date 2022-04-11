from cgitb import html
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

    #Read and feth the server in Servers database.
    serverdb = "SELECT server FROM Servers"
    servers = cursor.execute(serverdb)
    servers = servers.fetchall()

    #Convert server tuples to list via list comprehension
    server_list = [server[0] for server in servers]
    print(server_list)


    return render_template("index.html", author_list=author_list, server_list=server_list)


#Card Profile Config
@app.route("/card")
    
def cardconfig():  

    #Configure App to connect with the SQLite Database
    connection = sqlite3.connect('appd.db')
    cursor = connection.cursor() 

    #Read and fetch Products in the database.
    readdb = "SELECT PRODUCT_name FROM Products"
    products = cursor.execute(readdb)
    products = products.fetchall()

    #Convert product tuples to list via list comprehension
    productNames = [product[0] for product in products]
    print(productNames)
    
    return render_template("cardconfig.html", productNames=productNames)


@app.route("/pprofile")

def productionProfile ():

    return render_template("productionProfile.html")

@app.route("/additional")

def additionalReq ():
    
    return render_template("additionalreq.html")
