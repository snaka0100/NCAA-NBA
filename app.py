from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)

# connect to mongo db and collection
#db = client.store_inventory
#produce = db.produce


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    #inventory = list(produce.find())
    #print(inventory)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("datapage.html")


if __name__ == "__main__":
    app.run(debug=True)
