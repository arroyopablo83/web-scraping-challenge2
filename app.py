from flask import Flask, render_template, redirect
from scrape import scrape
import pymongo

app = Flask(__name__)

@app.route("/scrape")
def scrape2():

    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    data = scrape()

    db = client.mars.mars1

    db.insert_one(data)

    return redirect("/", code=302)

@app.route("/")
def index():
    
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars.mars1
    data = db.find_one()

    print(data)
    print(type(data["mars_facts"]))
    #type(data["hemisphere_image_urls"][1])
    #urlimagenes = [i["img_url"] for i in data["hemisphere_image_urls"]]
    u_img = [data["hemisphere_image_urls"][i]["img_url"] for i in range(len(data["hemisphere_image_urls"]))]

    return render_template("index.html", headlines=data["headlines"], imageMars=data["imageMars"], mars_facts=data["mars_facts"], hemisphere_image_urls=u_img)

if __name__ == "__main__":
    app.run(debug=True)