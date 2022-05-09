from cgitb import html
from flask import Flask, flash, redirect, render_template, request, session, url_for
import sqlite3
import os
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

#Current Directory of the project
currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#Homepage
@app.route("/", methods=["POST", "GET"])
def home():

    #Configure App to connect with the SQLite Database
    con = sqlite3.connect('appd.db')
    cur = con.cursor()
    
    #Read and fetch the Author_name in the database
    readdb = "SELECT AUTHOR_name FROM Author"
    authors = cur.execute(readdb)
    authors = authors.fetchall()


    #Convert author tuples to list via list comprehension
    author_list = [author[0] for author in authors]
    print(author_list)

    #Read and feth the server in Servers database.
    serverdb = "SELECT server FROM Servers"
    servers = cur.execute(serverdb)
    servers = servers.fetchall()

    #Convert server tuples to list via list comprehension
    server_list = [server[0] for server in servers]
    print(server_list)

    if request.method == "POST":
        print("This is POST!")
        name = request.form["projName"]
        author_select = request.form["author_select"]
        version_select = request.form["version_select"]
        projectNum = request.form["projectNum"]
        product_select = request.form.get("product_select")
        cps_version = request.form["cps_version"]
        service_pack = request.form["service_pack"]
        cps_version1 = request.form["cps_version1"]
        service_pack1 = request.form["service_pack1"]
        cps_server = request.form.get("cps_server")
        cps_server1 = request.form.get("cps_sever1")
        
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(name)
        print(author_select)
        print(version_select)
        print(projectNum)
        print(product_select)
        print(cps_version)
        print(service_pack)
        print(cps_version1)
        print(service_pack1)
        print(cps_server)
        print(cps_server1)
        print(time)

        #INSERT values into the Project Database
        cur.execute("INSERT INTO Project (PROJECT_id, PROJECT_name, AUTHOR_name, VERSION_id, PRODUCT_type, CPS_version, SERV_pack, CPS_server, UPLOAD_time) VALUES (?, ?, ?, ?, ?, ?, ? , ?, ?)", [projectNum, name, author_select, version_select, product_select, cps_version, service_pack, cps_server, time])
        print("INSERTED Successfully!")

        #Commit our con
        con.commit()

        #Close our con
        con.close()
   
        return redirect("/card")
    else:
        print("This is a GET!")
        return render_template("index.html", author_list=author_list, server_list=server_list)


#Card Profile Config
@app.route("/card", methods=["POST", "GET"])
    
def cardconfig():  

    #Configure App to connect with the SQLite Database
    con = sqlite3.connect('appd.db')
    cur = con.cursor() 

    #Read and fetch Products in the database.
    readdb = "SELECT PRODUCT_name FROM Products"
    products = cur.execute(readdb)
    products = products.fetchall()

    #Convert product tuples to list via list comprehension
    productNames = [product[0] for product in products]
    print(productNames)

    if request.method == "POST":
        app = request.form["app"]
        applet = request.form["applet"]

        print("This is a POST!")
        print(app)
        print (applet)


        return redirect("/pprofile")
    else: 
        return render_template("cardconfig.html", productNames=productNames)


@app.route("/pprofile", methods=["POST", "GET"])

def productionProfile ():

    return render_template("productionProfile.html")

@app.route("/additional", methods=["POST", "GET"])

def additionalReq ():
    
    return render_template("additionalreq.html")
