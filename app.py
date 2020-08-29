import os
from flask import Flask, render_template, redirect, request, url_for
if os.path.exists("env.py")
    import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DB_NAME"] = "dictionary_manager"
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster.r2bey.mongodb.net/dictionary_manager?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')


@app.route("/get_index")
def get_dictionary():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
