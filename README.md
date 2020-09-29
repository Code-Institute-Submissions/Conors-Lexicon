# ***Conors Lexicon***

Conor's Lexicon is a website that is dedicated to those who want to create new Words, Idioms, proverbs etc and share their creation to the rest of the world in the hopes of their world going viral.The website allows people to create
a dictionary that anyone with a user profile is able to use use CRUD (create, read, update, delete) to enrich the database that is supported by MongoDB.

The Admin is able to use CRUD on all words, while other users can only update and delete words that they've made themselves.


# UX 

**In theory, Conor's Lexicon can be enjoyed by anyone:** It can have words that varies from your run of the mill proverbs that most people have already heard about to the more edgier Urban dictionary level of ridiculous entries.
Here are some realistic scenarios that users will face when using the website.

**As A user, I want to Read entries that other users have submitted:** Perfect, On every single page there is a search bar letting them look up what ever they had in mind. The user should type either the word category (noun, proverb etc), the word 
itself the word definition or a tag that's associated with the word. Upon pressing enter, they will either see a range of words matching their criteria or an error message in red saying no results found.

**As a user, I want to add a new word to the Lexicon:** This one is a lot more complicated, especially if they havent set up an account yet. Let's assume they havent so I can demonstrate how to do that. First off, the user will need to click the Register
button in the navbar, just above the Search bar.Next, they must fill out the form with thier name, a unique username,a valid email address, their continent they currently reside in, Their password which is accepted by the website and finally confirm that
password by reentering it again. If all goes well, they will get a message saying that they've sucessfully registered their account. Otherwise, they will need to fix any errors they made during the registration. If the user already has registered 
for an account prior, They can instead click the Log in Button instead of register. From their, they will need to enter their email address and password that they registered with. It could also be the case that the user was already logged in.
No matter the case, fulfilling any three of those scenarios should result in an extended nav list at the top middle of the page. To get started on creating a new word, the User should click New Word. From here, they much choose the word category,
followed by the word name. After that, they should define the word and demonstrate it in a sentence. Finally, They should apply an appropriate Tag to aid other users finding this word. After clicking the Add Word Button, they should see their new 
added to the website.

**As a user, I want to delete a word:** As stated previously, the user can only delete words that they have created themselves, unless the user is an admin. They must also have a registered account and logged into the website, there is a tutorial on how
to do that above. Next to the word that they've created should be a delete button. Upon clicking it, they should see in green text that the word has been deleted. It now no longer can be found on the website or the backend database.

**As a user, I want to update a word:** Assuming the user is logged in,go to where your word is and click the edit button. From here, you're presented the same form you saw when you made the word with it filled in exactly as you left it. Simply add or remove the text you want and 
click the edit button at the end of the form. Alternatively, the user can click cancel and go back to the Index page.



# Features

### On Base Template

**Navbar:** The most fundamental part of my website, it allows users to navigate to different pages, from logging in to Creating a new Word.

**Search Index:** This allows for read users to search for the word that they want, be it through the name, the category, its definition or an associated tag.

**Footer**:


### On index page 


### add_word Template

**Create a new word:** Gives the user a form to create a new word and add it to the database, they need to fill out its category, word name, description, demostrate its use in a sentence and finally apply a tag for better index searching. Must be
logged in to see this page on the navbar.

### Register Template

**Register a new account:** A User that is logged out of the system is able to create a fresh account. They must fill out the form giving their name, a uhique username that hasn't been registered on the website before,
 a valid email address, their continent of residence and a password with ________ . Must be logged out to see this page on the navbar.

### Login Template

**Login into an existing account:** A user who is logged out of the system but has already registered an account prior will be able to log in. They need only give their username and password and click the Login Button. They will see the page
only if they're logged out.

### Profile Template 

**View your unique profile:** When the user is logged in, they will be able to see their profile page link on the navbar. From there, they will see the details they entered upon registering as well as ________

### Update Template 

**Update words the user has made:** When the user see's their word on their website, they'll have the option of updating various fields in it by clicking on the Edit button next to the word. From here they can change the fields of the word, the same
ones from the add_word template. Must be logged in to update.

### how it works template 


## Features left to implement 



# Technologies used 

Html 5: This language is used to present content on my website.

Css: Css is used for styling the webpage, thus making it more attractive to the user if used correctly.

[Materializecss:](https://materializecss.com/) Used for its Grid System, useful pre build classes and its componenets. Some of its componenets I borrowed was a pre built nav bar and its pre build footer. Not only does it save time, It looks really
good too.

[Google Fonts:](https://fonts.google.com/) I imported and used the Lora, Playfair-display, Montserrat and Parisienne fonts from Font awesome.

[Font Awesome:](https://fontawesome.com/) Many of the Icons used in my website are from font Awesome, such as the ones in Registration and add_word templates.

[JQuery:](https://jquery.com/) JQuery is a javascript Library that allows us to use a method as a shorthand way of writing many lines of javascript code. Much of My JS code borrowed from materializecss requires Jquery.

[Flask:](https://flask.palletsprojects.com/en/1.1.x/) A python framework used for web development.

[Heroku:](https://www.heroku.com/) A cloud based program that is used to deploy my website.It supports the Python Programming Language.

# Testing

# Deployment


# Credits

## Content 

* My Navbar for both small and larger screenwidths, alongside the Footer, came from Materializecss.

* The code for my search index bar can be found on [freefrontend.com](https://freefrontend.com/jquery-search-boxes/).

* In general I must thank Code Institute  for the tutorial lessons as it gave me the appropriate code to build the bare bones of my website.


## Media 



## Acknowledgements 

* I got some ideas for some of my font pairings from [Quicksprout.com](https://www.quicksprout.com/best-font-for-website/).

* Code institute will be thanked again as the newly updated video series gave me the idea to make the Registration page, Login page and also the profile page.










admin password:admin123