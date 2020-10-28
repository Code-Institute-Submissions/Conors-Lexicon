import os
from flask import (
    Flask, render_template,
    redirect, request,
    url_for, flash, session)
from flask_pymongo import PyMongo
import datetime
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
@app.route("/home")
def home():
    words = mongo.db.words.find().sort("views", -1).limit(10)
    x = datetime.datetime.now()
    print(f"now: {x}")
    current_date = x.strftime("%d/%m/%Y")
    print(f"now string: {current_date}")
    timeDb = mongo.db.time.find_one({"_id": ObjectId(
        "5f9836072ead5e960e82ec42")})
    print(f"timeDb: {timeDb}")
    if timeDb["date"] == current_date:
        time_word = mongo.db.time.find_one({
            "_id": ObjectId("5f9836072ead5e960e82ec42")})
        word_of_the_day = time_word["word"]
    else:
        word_daily_swap = list([word for word in mongo.db.words.aggregate(
         [{"$sample": {"size": 1}}])])
        change = {
                    "word": word_daily_swap,
                    "date": current_date
        }
        mongo.db.time.update({"_id": ObjectId(
        "5f9836072ead5e960e82ec42")}, change)
        time_word = mongo.db.time.find_one({
            "_id": ObjectId("5f9836072ead5e960e82ec42")})
        word_of_the_day = time_word["word"]


    return render_template("index.html", words=words, word_of_the_day=word_of_the_day)


@app.route("/word/<word_id>")
def word(word_id):
    words = mongo.db.words.find({"_id": ObjectId(word_id)})
    temp_word = {}
    for word in words:
        temp_word = word

    print(temp_word)
    temp_word['views'] = int(temp_word['views'] + 1)
    mongo.db.words.update({"_id": ObjectId(word_id)}, temp_word)
    words = mongo.db.words.find({"_id": ObjectId(word_id)})

    return render_template("word.html", words=words, temp_word=temp_word)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    if len(words) == 0:
        flash("sorry, there are no results for your query. Please try again.")
        return redirect(url_for("home"))

    else:
        flash("Results:")

    return render_template("search-results.html", words=words)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        passwordConfirm = request.form.get("passwordConfirm")
        if password == passwordConfirm:
            register = {
                "name": request.form.get("name").lower(),
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "location": request.form.get("location"),
                "password": generate_password_hash(password)
            }

            mongo.db.users.insert_one(register)

        else:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home"))
    return render_template("register.html")


@app.route("/update_user/<user_id>", methods=["GET", "POST"])
def update_user(user_id):
    if request.method == "POST":

        submit = {
            "name": request.form.get("name").lower(),
            "username": session["user"].lower(),
            "email": request.form.get("email").lower(),
            "location": request.form.get("location").lower(),
            "password": session["user"].lower()
        }

        mongo.db.users.update({"_id": ObjectId(user_id)}, submit)
        flash("Your Profile details have been changed")
        return redirect(url_for("home"))

    user_update = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("update-user.html", user_update=user_update)


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
                return redirect(url_for("home"))

            else:

                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if "user" in session:

        words = list(mongo.db.words.find())
        username = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template("profile.html", username=username, words=words)
    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))


@app.route("/logout")
def logout():

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if "user" in session:
        if request.method == "POST":
            created_by = "anonymous" if request.form.get(
                "created_by") else session["user"]
            views = 0
            word = {
                "category_name": request.form.get("category_name"),
                "word_name": request.form.get("word_name"),
                "word_definition": request.form.get("word_definition"),
                "word_in_sentence": request.form.get("word_in_sentence"),
                "tags": request.form.get("tags"),
                "created_by": created_by,
                "views": views
            }
            mongo.db.words.insert_one(word)
            flash("Word Successfully Added")
            return redirect(url_for("home"))
    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))

    word_type = mongo.db.word_type.find().sort("category_name", 1)
    return render_template("add_word.html", word_type=word_type)


@app.route("/error")
def error():
    return render_template("error.html")


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    if "user" in session:
        if request.method == "POST":
            created_by = "anonymous" if request.form.get(
                "created_by") else session["user"]

            submit = {
                "category_name": request.form.get("category_name"),
                "word_name": request.form.get("word_name"),
                "word_definition": request.form.get("word_definition"),
                "word_in_sentence": request.form.get("word_in_sentence"),
                "tags": request.form.get("tags"),
                "created_by": created_by
            }
            mongo.db.words.update({"_id": ObjectId(word_id)}, submit)
            flash("Word Successfully Updated")
            return redirect(url_for("home"))
    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))

    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    word_type = mongo.db.word_type.find().sort("category_name", 1)
    return render_template("update.html", word=word, word_type=word_type)


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.words.remove({"_id": ObjectId(word_id)})
    flash("word deleted")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
