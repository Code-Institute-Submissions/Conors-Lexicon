import os
from flask import (
    Flask, render_template,
    redirect, request,
    url_for, flash, session)
from flask_pymongo import PyMongo  # required to communicate with mongodb
import datetime
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash # keeps the password field value to be hashed on mongodb for added security for the websites user.
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
  # This function does two different things, the first and straightforward one is to 
  # sort the words collection by the amount of views in descending order it has and
  # limits the results to 10. We must use the sort and limit methods to achieve this. Next, we will change word of the day on the index page to change daily.
  # We achieve this by importing datetime above, then we set a variable to equal the current time.
  # We convert it to a string and compare it to the value inside the date field on MongodB. A new word is chosen if the dates dont match,
  # otherwise the word is picked from the word field in the time collection.

    words = mongo.db.words.find().sort("views", -1).limit(10)
    time_import = datetime.datetime.now()
    current_date = time_import.strftime("%d/%m/%Y")
    timeDb = mongo.db.time.find_one({"_id": ObjectId(
        "5f9836072ead5e960e82ec42")})
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
    # the word_id variable is assigned as word._id in the html page and is
    # carried over upon clicking the hyperlink on the word name itself,
    # it will bring the accompanying ID. This is important because it
    # allows us to load the correct word from the collection.
    words = mongo.db.words.find({"_id": ObjectId(word_id)})
    # now dymanically load the word by passing through
    # the varialbe word_id and assign that to the object ID in the find method.
    temp_word = {}
    for word in words:
        temp_word = word

    temp_word['views'] = int(temp_word['views'] + 1)
    mongo.db.words.update({"_id": ObjectId(word_id)}, temp_word)
    # to incriment the word field by 1, I must first create a new varialble
    # called temp_word, I will iterate through the words collection that copies
    # the value of all the entries. Each entry in words collection is
    # incremented by one, however I will only update the entry with the
    # associated word_id. I will now display the word object again
    # with its new view value.
    words = mongo.db.words.find({"_id": ObjectId(word_id)})

    return render_template("word.html", words=words, temp_word=temp_word)


@app.route("/search", methods=["GET", "POST"])
def search():
    # query variable is used to assign it to the input
    # value of the search bar, we will be using a text search iterating over
    # the words collection, the value will be the query, aka the value inside
    # the search bar. If there are no results,
    # I will notifty the user asking them to try again.
    # Otherwise the results are displayed.
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
    if "user" not in session:
        if request.method == "POST":

            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("register"))
                # defensive programming at display here,  assigns existing_user
                # variable to the entered username value, if its found in the
                # database, then upon hitting the register button the user
                # will get a flash message saying the user exists and will
                # be redirected back at the register page.

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
                # assigns the password and passwordConfirm to two variables of
                # the same name, if they're the same then a register variable is
                # created with all the form values, it is then inserted into the
                # database using the insert_one method. The password is protected
                # and cant be seen on MongoDb by importing generate_password_hash
                # from werkzeug.security

            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("home"))

    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))
            # the new user will be logged by importing session from flask
            # and applying that here, you'll be redirected to the homepage.
    return render_template("register.html")


@app.route("/update_user/<user_id>", methods=["GET", "POST"])
def update_user(user_id):
    # very similiar to the process above, except the username and password
    # cannot be changed. we use the update method with the submit varialbe
    # to change the profile details, we use session from flask to get the
    # username and password values. For the rest, the values are obtained
    # from the form that is posted on the webpage.
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
    if "user" not in session:
        if request.method == "POST":

            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # check_password_hash is a Werkzeug security helper that
                # compares the hashed value of the form value and the database
                # value. The user will be logged in here and will be redirected
                # to the homepage with welcome message to have their own
                # username appear on screen.
                if check_password_hash(
                        existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("home"))
                else:

                    flash("Incorrect Username and/or Password")
                    return redirect(url_for("login"))

            else:
                # their are two types of errors that can happen during login,
                # an incorrect username or password. I check for both with these
                # two if statements, if either value is incorrect, I will display
                # the exact same error message. This is important for defensive
                # design as a hacker, for example, wouldn't be able know which
                # part they entered correctly/incorrectly.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # the if statement is there to provide defensive programming,
    # without this if statement anyone can theoretically access the
    # profile of another user, weather they're signed in or not.
    # There must be a user in session to open this page, if you
    # try to access the admin page when signed in as someone else,
    # it will redirect youur profile details instead, otherwise the error
    # function will be called opening error.html saying access forbidden.
    # We bring the words and username variables to the
    # html page so we can display profile details and words that the user
    # has made on the webpage.
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
    # removes the user from the session cookies,essentially logging them
    # out on a refresh, or in this case redirecting them to a new page.


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    # will set the value of this variable to anonymous if the box is
    # checked on the browser, otherwise it will be the username in
    # session value. Views is initalised here as I had issues setting
    # its value inside the word variable.
    if "user" in session:
        if request.method == "POST":
            created_by = "anonymous" if request.form.get(
                "created_by") else session["user"]
            views = 0
            # using key value pairs from the words collection fields and the
            # form data aswell as the two aforementioned variables. the word
            # variable is inserted into the words collection on mongodb as a
            # new object and the user is redirected to the home page.
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
    # purpose of this function is to display a forbiden 403
    # error for defensive programming purposes, more is explained inside the
    # login function
    return render_template("error-403.html")


@app.errorhandler(404)
def page_not_found_404(e):
    return render_template('error-404.html'), 404


@app.errorhandler(500)
def page_not_found_500(e):
    return render_template('error-500.html'), 500


@app.route("/update_word/<word_id>", methods=["GET", "POST"])
def update_word(word_id):
    if "user" in session:
        if request.method == "POST":
            created_by = "anonymous" if request.form.get(
                "created_by") else session["user"]
            views = mongo.db.words.find_one({"_id": ObjectId(word_id)})
            views = views["views"]
            # setting the value of views to be the current one inside the word
            # Object. We set every single value otherwise it wouldn't be
            # included in the updated object.
            submit = {
                "category_name": request.form.get("category_name"),
                "word_name": request.form.get("word_name"),
                "word_definition": request.form.get("word_definition"),
                "word_in_sentence": request.form.get("word_in_sentence"),
                "tags": request.form.get("tags"),
                "created_by": created_by,
                "views": views
            }
            # process is similiar to adding a word, except we use the update
            # method and add the submit varialbe to update the appropriate
            # word_id fields
            mongo.db.words.update({"_id": ObjectId(word_id)}, submit)
            flash("Word Successfully Updated")
            return redirect(url_for("home"))

    else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))
# the word ID is brought over upon clicking the edit button on the browser,
# which allows us to both edit the details of that specific object and
# to have the form data already filled in on update.html.
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    word_type = mongo.db.word_type.find().sort("category_name", 1)
    return render_template("update.html", word=word, word_type=word_type)


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    # we carry over the appropriate word Id field and use the
    # remove method to delete it from both the database and the website.
    mongo.db.words.remove({"_id": ObjectId(word_id)})
    flash("word deleted")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
