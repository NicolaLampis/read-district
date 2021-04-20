# Read District

This website provide book reviews and recommendation.
You can write your personal review and read review of other users.
Here you can find a selection of great book you'll love.
 
## UX
 
## UX (User Experience) ##

### **Project Goals** ###

The **goal** of this project is to build a website, using backend knowledge, to allows users to read book reviews
created by other registered users and write book reviews.

The **features** on the website will:

- Display a list of book reviews containing book information.
- Display all the details of each book and their review.
- Visitors can see the reviews and can register a user account.
- A registered user create their own book reviews and edit them.

I achieve this by:

- Providing registration functionality. A Registration form with username and password allow the user to create an account.
- Providing log in functionality. Users can log in to their account.
- With backend technologies the website display and grant access to the data stored into the MongoDB database.
- Enabling users who are logged in to create, edit or delete their own book reviews.

### **User Goals** ###

- **Read** book reviews created by other users.
- **Search** book reviews.
- **Create** book reviews, share a personal point of view with other readers.
- **Update** apersonal book review.
- **Delete** a book review.

### **User Stories** ###


#### **New Site Visitor** ####

- As a **user**, I want to see a **navigation bar** always visible, that helps me to navigate to the site pages.
- As a **user**, I want to see a complete list of the available book reviews.
- As a **user**, I want to interact with the book cards to see more info about the book reviews displayed.
- As a **user**, I want to be able to **search** for book reviews.
- As a **user**, I want to **register** to the site with a personal username and password.
- As a **user**, I want to be able to **log in** to the site.
- As a **user**, I can contact the site owner(s) using GitHub.
- As a **user**, I want a responsive app on mobile devices as well as desktop screen.


#### **Returning Site Visitor** ####

- As a **user**, I want to see my user account profile page.
- As a **user**, I want to create, edit or delete my own book reviews.


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used


### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website


### **Database** ###

- [MongoDB Atlas](https://www.mongodb.com/)
  - Cloud based document-oriented database used to store the backend data.

### **Libraries** ###

- [MaterializeCSS](https://materializecss.com/)
  - Used to design a mobile-first responsive website layout.
- [Flask](https://www.fullstackpython.com/flask.html)
  - Python web framework
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
  - A comprehensive WSGI web application library installed with Flask
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
  - PyMongo is a Python tool for working with MongoDB
- [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/)
  - Flask-PyMongo bridges the gap between Flask and PyMongo
- [DNSPython](https://www.dnspython.org/)
  - DNS toolkit for Python
- [itsdangerous](https://pypi.org/project/itsdangerous/)
  - Python utility for hash-based message authentication installed with Flask(HMAC, SHA-512)
- [jQuery](https://jquery.com/)
  - Used for the initialisation of the Materialize CSS components functionality.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - Templating language for Python.



### **Tools** ###

- [Git](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - Used to store, host and deploy the project files and source code after being pushed from Git.
- [Gitpod](https://www.gitpod.io/)
  - An online IDE linked to the GitHub repository used for the majority of the code development.
- [Visual Studio Code](https://code.visualstudio.com/)
  - A locally installed IDE connected to the GitHub repository for when there was no internet connection to use Gitpod.
- [Google Material Icons](https://fonts.google.com/icons?selected=Material+Icons)
  - Used for icons to enhance headings and add emphasis to text.
- [Google fonts](https://fonts.google.com/)
  - Used for the website fonts.
- [Color Gradient Generator](https://cssgradient.io/)
  - An online tool used to choose the website colour scheme.
- [Am I Responsive?](http://ami.responsivedesign.is/)
  - A tool for taking a quick snapshot of the responsive breakpoints of the website to visualize how the site will look on different device screen sizes in one place. The resulting screenshot is also used as the README.md logo image.
- [Adobe Illustrator](https://en.wikipedia.org/wiki/Adobe_Photoshop) xxx
  - A raster graphics editor used to manipulate the clock face background image.
- [randomkeygen.com](https://randomkeygen.com/)
  - Random secure password & keygen generator used to create the Flask SECRET_KEY.


[Back to contents](#contents)


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X