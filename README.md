# ***Conors Lexicon***

Conor's Lexicon is a website that is dedicated to those who want to create new Words, Idioms, proverbs etc and share their creation to the rest of the world in the hopes of their world going viral.The website allows people to create
a dictionary that anyone with a user profile is able to use use CRUD (create, read, update, delete) to enrich the database that is supported by MongoDB.

The admin account is able to use CRUD on all words, while other users can only update and delete words that they've made themselves. The Log in details for this account is username "admin" and password "admin123". I recommend using both this account and creating
your own while on the site.

![Image of Book](https://ibb.co/ypBPXZn)

# MongoDB 


**Collections and their fields:** I decided to add this section to add clarity to my collections on MongoDB. The main one you'll see is the words collection, you can interact with this collection on the website by creating new words, editing words, deleting words, reading them
or viewing them to add an extra view. We have the time collection, which has a word field that has an object from the words collection, and a date field which will change daily upon a reload on the index page. word_type field is next, it is linked to words collection
and you can interact with it by creating or editing a word. Last and not least we've the users collection, which can also be read, updated and edited. 

Below I've supplied fields and values you'd expect to see in my website:

* [Words](https://ibb.co/M8qhqGY)
* [Time](https://ibb.co/T8dwF4t)
* [Word_type](https://ibb.co/cJvZtFq)
* [Users](https://ibb.co/WFr6vfM)

# UX 


**In theory, Conor's Lexicon can be enjoyed by anyone:** It can have words that varies from your run of the mill proverbs that most people have already heard about to the more edgier Urban dictionary level of ridiculous entries.

**As A user, I want to Read entries that other users have submitted:** Perfect, On every single page there is a search bar letting them look up what ever they had in mind. The user should type either the word category (noun, proverb etc), the word 
itself the word definition or a tag that's associated with the word. Upon pressing enter, they will either see a range of words matching their criteria or an error message saying no results found. The home page will pre select the 10 most viewed words, this can
be manipulated by the user.

**As a user, I want to add a new word to the Lexicon:** This one is a lot more complicated, especially if they havent set up an account yet. Let's assume they haven't so I can demonstrate how to do that. First off, the user will need to click the Register
button in the navbar, just above the Search bar.Next, they must fill out the form with their name, a unique username,a valid email address, their continent they currently reside in, Their password which is accepted by the website and finally confirm that
password by re entering it again. If all goes well, they will get a message saying that they've successfully registered their account. Otherwise, they will need to fix any errors they made during the registration. If the user already has registered 
for an account prior, They can instead click the Log in Button instead of register. From their, they will need to enter their email address and password that they registered with. It could also be the case that the user was already logged in.
No matter the case, fulfilling any three of those scenarios should result in an extended nav list at the top middle of the page. To get started on creating a new word, the User should click New Word. From here, they must choose the word category,
followed by the word name. They will then demonstrate its use in a sentence. Using it in a sentence and applying a tag is optional. After clicking the Add Word Button, they should see their new word in the profile view or by searching for it, as shown above.
added to the website.

**As a user, I want to delete a word:** As stated previously, the user can only delete words that they have created themselves, unless the user is an admin. They must also have a registered account and logged into the website, there is a tutorial on how
to do that above. Next to the word that they've created should be a delete button. Upon clicking it, a modal will appear and they must click yes to confirm the deletion. It now no longer can be found on the website or the back end database.

**As a user, I want to update a word:** Assuming the user is logged in,go to where your word is and click the edit button. From here, you're presented the same form you saw when you made the word with it filled in exactly as you left it. Simply add
or remove the text you want and click the edit button at the end of the form. Alternatively, the user can click cancel and go back to the Index page.

**As a user, I want to update my profile details:** Assuming they're already logged in, they should click the profile view and then the edit button that appears below their details. They're presented with some of the same fields as before, excluding the username and
password. They can submit the details or click cancel to go back to the profile page.


# Features

### On Base Template

**Navbar:** The most fundamental part of my website, it allows users to navigate to different pages, from logging in to Creating a new Word.

**Search Index:** This allows for read users to search for the word that they want, be it through the name, the category, its definition or an associated tag.

**Footer:** At the end of the webpage, you have a footer. None of the nav links are working.


### On index.html page

**See the word of the day:** A word is randomely chosen daily and will update when the date changes on the global clock that datetime uses. The function must also be called for this to happen, ie. a refresh on the index page.

**See trending words:** The top 10 trending words will appear as well. It is sorted by the amount of views each word has. A user could manipulated this view count by clicking on the word name which will add 1 to view.

Below are some Wireframes for index.html:

* [Desktop](https://ibb.co/m0YBbd9)
* [Tablet](https://ibb.co/S6mXrQ7)
* [Mobile](https://ibb.co/cr2021B)


### add_word Template

**Create a new word:** Gives the user a form to create a new word and add it to the database, they need to fill out its category, word name, description, optionally demonstrate its use in a sentence and finally apply a tag for better index searching, if they wish.
There is also the option to post the word anonymously, however this will mean they wont be able to edit or delete the word themselves. Must be logged in to see this page on the navbar.

Below are some Wireframes for add_word.html:

* [Desktop](https://ibb.co/s1KwXNB)
* [Tablet](https://ibb.co/NSVPVwX)
* [Mobile](https://ibb.co/18RPL23)


### Register Template

**Register a new account:** A User that is logged out of the system is able to create a fresh account. They must fill out the form giving their name, a unique username that hasn't been registered on the website before,
 a valid email address, their continent of residence , a password and a password confirmation that matches the password field. Must be logged out to see this page on the navbar.

 Below are some Wireframes for register.html:

* [Desktop](https://ibb.co/xDGLyXN)
* [Tablet](https://ibb.co/NNBpgJb)
* [Mobile](https://ibb.co/YtrHK6S)


### Login Template

**Login into an existing account:** A user who is logged out of the system but has already registered an account prior will be able to log in. They need only give their username and password and click the Login Button. They will see the page
only if they're logged out.

Below are some Wireframes for login.html:

* [Desktop](https://ibb.co/6gFQ5bj)
* [Tablet](https://ibb.co/DKYxK4V)
* [Mobile](https://ibb.co/sq9rzcS)


### Profile Template 

**View your unique profile:** When the user is logged in, they will be able to see their profile page link on the navbar. From there, they will see the details they entered upon registering as well as the words that they've created, Assuming
they chose not to post the word anonymously.

Below are some Wireframes for profile.html:

* [Desktop](https://ibb.co/F5SJq5j)
* [Tablet](https://ibb.co/yhc218C)
* [Mobile](https://ibb.co/FWS05j4)


### Update Template 

**Update words the user has made:** When the user finds their word on the website, be it on the homepage, by searching or in their profile view, they'll have the option of updating various fields in it by clicking on the Edit button next to the word.
From here they can change the fields of the word, the same ones from the add_word template. Must be logged in to update. No wireframe included as its almost identical to add_word.html, apart from the buttons.

### error template 

**Displays an error when the user tries to go somewhere where they shouldn't:** If for example, you enter into the url /(username) of someone they're not logged in as, instead of showing you their profile, you'll instead be shown an error page telling them they 
shouldn't be here. This will also display for add_word.html. If the user is logged in but enters the url to register or log in, they'll also see this page.

Below is a wireframe for error.html, there is little to no difference

* [Desktop](https://ibb.co/nkbnMqh)
* [Tablet](https://ibb.co/bdKYDsR)
* [Mobile](https://ibb.co/WDBLv9J)


### Word Template 

**View a word as a single entity:**  Clicking on the word name will bring it up as its own seperate page. The purpose of this is to isolate the word and also to give the view value of +1. This is important because it will dictate what trending words you'll see 
on the index page.

Below are some Wireframes for word.html:

* [Desktop](https://ibb.co/Mhm1Tvz)
* [Tablet](https://ibb.co/pXTQMqt)
* [Mobile](https://ibb.co/G3LghLS)


## Features left to implement 


**Add more features to word.html:** I've demonstrated the use of import time before, I could of had it display when the word was created when clicking on the word. Also, I could've combined the view and time functionalities I've showed off before to see how many
views a word had in a certain time period. For example, the most viewed word of the day, week, month etc.

**The option to change password:** In update details, I could have given the user the option to change password. However, it required far greater degree of thought. For example, would I have to make the user enter their previous passowrd to change their current one?
Which fields would be required? How exactly would it be implemented using if statements etc? I showed a similar skill set on password confirmation during registration, ultimately I didn't have time to implement this feature.


# Technologies used 

Html 5: This language is used to present content on my website.

Css: Css is used for styling the web page, thus making it more attractive to the user if used correctly.

[Materializecss:](https://materializecss.com/) Used for its Grid System, useful pre build classes and its componenets. Some of its componenets I borrowed was a pre built nav bar and its pre build footer. Not only does it save time, It looks really
good too.

[Google Fonts:](https://fonts.google.com/) I imported and used the Lora, Playfair-display, Montserrat and Parisienne fonts from Font awesome.

[Font Awesome:](https://fontawesome.com/) Many of the Icons used in my website are from font Awesome, such as the ones in Registration and add_word templates.

[JQuery:](https://jquery.com/) JQuery is a javascript Library that allows us to use a method as a shorthand way of writing many lines of javascript code. Much of My JS code borrowed from materializecss requires Jquery.

[Flask:](https://flask.palletsprojects.com/en/1.1.x/) A python framework used for web development. Used for rendering templates, flash messages, redirects etc

[Heroku:](https://www.heroku.com/) A cloud based program that is used to deploy my website.It supports the Python Programming Language.

[Werkzeug:](https://werkzeug.palletsprojects.com/en/1.0.x/) For generating password hash for security reasons.

[Datetime:](https://docs.python.org/3/library/datetime.html) Used to change the word of the day on the homepage.

# Testing

**As a user, I want to register an account:**

1. If you're already logged in, click on log out on nav bar. Skip this step if you're not logged in.
2. Click on register on the nav bar.
3. Fill out the form in many different variations, such as forgetting the @ in email address, using a different confirmed password to confirmed etc
4. Click on register
5. repeat these steps over and over to test defensive programming, also do the same on Opera and Firefox.

*Results:* Failure, confirmed password doesn't have to be the same as password, thus making it redundant. I decided to use an if statement to check if the two fields are the same. If they are, the user will be created. Otherwise, you'll get an error message 
stating that the passwords do not match.

```python
if "password" == "passwordConfirm":
            mongo.db.users.insert_one(register)

        else:
            flash("Passwords do not match")
            return redirect(url_for("register"))
```

**As a user, I want to log into an existing account:**

1. If you're already logged in, click on log out on nav bar. Skip this step if you're not logged in.
2. Click on Login in on the navbar,
3. Enter the correct Username and password and Log in.
4. repeat steps 1 and 2, now enter an incorrect username and/or password.

*Results:* Success, you are only logged in with both correct username and password with the appropriate flash message displaying if you succeeded or failed. However, I noticed that after logging in, it would be better to render the Index page instead of going back 
to the Login.

**As a user, I want to delete a word:**

1. If you're not already logged in, do so by clicking the nav link and filling out the form correctly.
2. If you have not done so already, create a word by clicking on new word and filling out the form and its fields. You can only delete words that you've made yourself, unless you're logged in as admin.
3. Search for words you're able to delete (ie. ones you've made yourself) either by using the search index or clicking on your profile.
4. Click on the delete button.
5. Ensure its deleted by searching for it in the index, checking your profile or looking at the words collection in MongoDB.

*Results:* Success, however there is a lack of defensive programming here, it's possible to accidentally  hit delete and have your word removed without you intending to do that. The delete button now calls for a modal where clicking on the yes button will delete the word.


**As a user, I want to update my profile:** 

1. If you're not already logged in, do so by clicking the nav link and filling out the form correctly.
2. Click  profile page in the nav links.
3. Underneath your profile details, click on the edit button.
4. Change the details in all fields and submit form.
5. Now check the profile page again and see if the details updated. Check MongoDB user collection as well.

*Results:* Failure, while im still logged in I cant see any details displaying and clicking on the edit button again gives me a url page not found error. However, on MongoDB my profile is updated. When I make a new word it actually says its created by the older username.
 I logged out and back in under the new username and password and it worked, giving me the new details. I realised I needed to update the cookies when changing the user details, so I added this line of python code in the update_user function. It fixed my problem.

```python

session["user"] = request.form.get("username").lower()

```

**As a defensive programmer, I want to see if I can access areas of my website that I should not be able to:**

1. If you're not already logged in, do so by clicking the nav link and filling out the form correctly.
2. Click on Profile Page, copy the url and now log out.
3. paste url into browser and press enter.
4. Repeat steps 1-3  and test update-user.html, update.html

*Results:* Success on all instances, I prompted the error.html page with the appropriate flask message. The python code that initialized  this page is below.


```python 
if "user" in session: (Execute code here)

else:
        flash("Woops, you aren't supposed to be here")
        return redirect(url_for("error"))
```

**As a user, I want to copy the word by using the copy button:**

1. Navigate to the home page.
2. Click on the Copy button in word of the day.
3. paste your new copied word somewhere
4. Repeat step 1-3 on the home page trending words, on search-results.html, word.html and profile.html.
5. Repeat steps 1-4 on Firefox and Opera.

*Results:* Failure, The word would only copy if it didnt have any spaces. I fixed it by changing the html id value value from {{ word.word_name }} to {{ word._id }} This new implementation fixed the code.

# Deployment



# Credits

## Content 

* My Navbar for both small and larger screen widths, alongside the Footer, came from Materializecss.

* The code for my search index bar can be found on [freefrontend.com](https://freefrontend.com/jquery-search-boxes/).

* In general I must thank Code Institute  for the tutorial lessons as it gave me the appropriate code to build the bare bones of my website.

* I got the copy functionality from [codepen.com](https://codepen.io/shaikmaqsood/pen/XmydxJ)


## Media 

* The cartoon book on the readme.md came from [adazing.com](https://www.adazing.com/book-clipart/)

* Error image came from [icon-icons.com](https://icon-icons.com/icon/close-remove-delete-warning-alert-error/93497)

## Acknowledgements 

* I got some ideas for some of my font pairings from [Quicksprout.com](https://www.quicksprout.com/best-font-for-website/).

* Code institute will be thanked again as the newly updated video series gave me the idea to make the Registration page, Login page and also the profile page.