from cgitb import html
from tkinter.font import ROMAN
from turtle import down
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


    #Read and fetch the server id and server in Server Database
    serverdict = "SELECT server_id, server FROM Servers"
    serverdict = cur.execute(serverdict)
    serverdict = serverdict.fetchall()

    #Convert the serverdict tuple to a dictionary
    server_dict= dict(serverdict)
    print(server_dict)

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
        cps_server1 = request.form.get("cps_server1")
        
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
        print(f"This is the CPS Server {cps_server} ")
        print(time)

        #INSERT values into the Project Database
        cur.execute("INSERT INTO Project (PROJECT_id, PROJECT_name, AUTHOR_name, VERSION_id, PRODUCT_type, CPS_version, SERV_pack, SERVER_id, UPLOAD_time) VALUES (?, ?, ?, ?, ?, ?, ? , ?, ?)", [projectNum, name, author_select, version_select, product_select, cps_version, service_pack, cps_server, time])
        print("INSERTED Successfully!")

        #Commit our con
        con.commit()

        #Close our con
        con.close()
   
        return redirect("/card")
    else:
        print("This is a GET!")
        return render_template("index.html", author_list=author_list, server_dict=server_dict)


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

    #Read and fetch Applications in the database.
    readdb = "SELECT APP_name FROM Applications"
    apps = cur.execute(readdb)
    apps = apps.fetchall()

    #Convert product tuples to list via list comprehension
    appNames = [app[0] for app in apps]
    print(appNames)
    


    if request.method == "POST":
        app = request.form["app"]
        applet = request.form["applet"]
        pseCheck = request.form.get('pseCheck')
        ppseCheck = request.form.get('ppseCheck')
        ndefCheck = request.form.get('ndefCheck')
        productName = request.form["productName"]
        maskRef = request.form.get('maskRef')
        atrConfig = request.form["atrConfig"]
        loaNum = request.form.get('loaNum')
        alcd = request.form.get('alcd')
        downsizing = request.form["downsizing"]
        tagRadio = request.form.get('tagRadio')
        fsRadio = request.form.get('fsRadio')
        sdRadio = request.form.get('sdRadio')
        tagText = request.form.get('tagText')
        fsText = request.form.get('fsText')

        print("This is a POST!")
        print(app)
        print (applet)
        print(pseCheck)
        print(ppseCheck)
        print(ndefCheck)
        print(productName)
        print(maskRef)
        print(atrConfig)
        print(loaNum)
        print(alcd)
        print(downsizing)
        print(tagRadio)
        print(fsRadio)
        print(sdRadio)
        print(tagText)
        print(fsText)


        return redirect("/pprofile")
    else: 
        return render_template("cardconfig.html", productNames=productNames, appNames=appNames)


@app.route("/pprofile", methods=["POST", "GET"])

def productionProfile ():

    if request.method == "POST":

        cusOffer = request.form['cusOffer']

        print(cusOffer)
        
        return redirect("/additional")

    else:
        return render_template("productionProfile.html")

@app.route("/additional", methods=["POST", "GET"])

def additionalReq ():
    
    return render_template("additionalreq.html")
