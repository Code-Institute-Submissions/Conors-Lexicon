import os
from flask import (
    Flask, render_template,
    redirect, request,
    url_for, flash, session)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DB_NAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route("/get_index")
def get_dictionary():
    words = list(mongo.db.words.find())
    words_rng = list([word for word in mongo.db.words.aggregate(
        [{"$sample": {"size": 1}}])])

    return render_template("index.html", words=words, words_rng=words_rng)


@app.route("/how_it_works")
def how_it_works():
    return render_template("howitworks.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    return render_template("index.html", words=words)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "name": request.form.get("name").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),

            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_dictionary"))

            else:

                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":

        word = {
            "category_name": request.form.get("category_name"),
            "word_name": request.form.get("word_name"),
            "word_definition": request.form.get("word_definition"),
            "word_in_sentence": request.form.get("word_in_sentence"),
            "tags": request.form.get("tags"),
            "created_by": session["user"]
        }
        mongo.db.words.insert_one(word)
        flash("Word Successfully Added")
        return redirect(url_for("get_dictionary"))

    word_type = mongo.db.word_type.find().sort("category_name", 1)
    return render_template("add_word.html", word_type=word_type)


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    if request.method == "POST":

        submit = {
            "category_name": request.form.get("category_name"),
            "word_name": request.form.get("word_name"),
            "word_definition": request.form.get("word_definition"),
            "word_in_sentence": request.form.get("word_in_sentence"),
            "tags": request.form.get("tags"),
            "created_by": session["user"]
        }
        mongo.db.words.update({"_id": ObjectId(word_id)}, submit)
        flash("Word Successfully Updated")

    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    word_type = mongo.db.word_type.find().sort("category_name", 1)
    return render_template("update.html", word=word, word_type=word_type)


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.words.remove({"_id": ObjectId(word_id)})
    flash("word deleted")
    return redirect(url_for("get_dictionary"))


@app.route("/word_type")
def word_type():
    word_type = list(mongo.db.word_type.find().sort("category_name", 1))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
