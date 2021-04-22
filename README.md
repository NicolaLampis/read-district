# Read District    

![Read District](wireframe/responsive.png)

This website provide book reviews and recommendation.
You can write your personal review and read review of other users.
Here you can find a selection of great book you'll love.


---

### **Contents** ###

- [UX (User Experience)](#ux-user-experience)
  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owner Goals](#site-owner-goals)
- [Design Choices](#design-choices)
  - [Fonts](#fonts)
  - [Colours](#colours)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Database](#database)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Additional Site Features](#additional-site-features)
  - [Site Construction](#site-construction)  
  - [Future Features](#future-features)
  - [Page Layout](#page-layout)
  - [Construction Table](#construction-table)
  - [Database Design](#database-design)
- [Project Management](#project-management)
- [Version Control](#version-control)
    - [Gitpod Workspaces](#gitpod-workspaces)
    - [Branches](#branches)
    - [Working within a branch](#working-within-a-branch)
    - [Merging branches in GitHub](#merging-branches-in-github)
    - [Update Gitpod with the latest GitHub commits](#update-gitpod-with-the-latest-github-commits)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Cloning the-reading-room from GitHub](#cloning-the-reading-room-from-github)
    - [Prerequisites](#prerequisites)
    - [Cloning the GitHub repository](#cloning-the-github-repository)
    - [Creation of a Python Virtual Environment](#creation-of-a-python-virtual-environment)
    - [Install the App dependencies and external libraries](#install-the-app-dependencies-and-external-libraries)
    - [Create the database in MongoDB](#create-the-database-in-mongodb)
    - [Create `env.py` file](#create-env.py-file)
    - [Run the application](#run-the-application)
  - [Deploying The Reading Room app to Heroku](#deploying-the-reading-room-app-to-heroku)
    - [Create the Heroku App](#create-the-heroku-app)
    - [Push your repository to GitHub](#push-your-repository-to-github)
    - [Connect Heroku to GitHub](#connect-heroku-to-github)
    - [Launch the App](#launch-the-app)
- [Credits](#credits)
  - [Images](#images)
  - [Colour](#colour)
  - [Inspiration](#inspiration)
  - [Acknowledgements](#acknowledgements)


---

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

### **Site Owner Goals** ###

- As a site owner, I want to create an interactive website that make use database and backend features as coding portfolio.
- As a site owner, I want to create a website for the user that want to share his /her personal opinions about books. 
- As a site owner, I want to create a website easy to use, safe for the user and his/her data.

[Back to contents](#contents)

--- 

## Design Choices ##

### **Fonts** ###

The main font I've chosen is [Crimson Pro](https://fonts.google.com/specimen/Crimson+Pro?selected=Material+Icons&query=crimson), 
is an antique-classic looking font that fit well with all type of books. It is sober and elegant.     
Is easy to read even using small font sizes.

### **Colours** ###

I've chosen for the backbround a color similar to the old paper, and a lighter tone for the serach bar and the cards.
Instead of a white background I wanted a warmer and relaxing color for the eyes.
I used strong accent of colors for text messages and buttons, because their function is to attract the attention.

![Colour Palette](wireframe/color-palette.png)

- (D7D7BE) - Navbar and a linear gradient for the bachground - black text
- (F5F5EE) - Card contents and search bar background - black text
- (284B5A) - Flash messages, primary color for the buttons and footer - white text
- (D84315) - Buttons cancel/delete - white text
- (616161) - Button cancel in the modal window - white text

### **Wireframes** ###

I designed the mock-ups of the website using [Figma](https://www.figma.com).

I designed the pages having in mind cards and forms from previous projects. This design works well with responsive behaviours.
The final result is slightly different, mostly improved by icons and organic repetition in the style.

- [Reviews Page](wireframe/books.png)
- [Review Page Mobile](wireframe/books-mobile.png)
- [Page of Book Review](wireframe/book-page.png)
- [Add a Review](wireframe/add-review.png)
- [Profile](wireframe/profile.png)


[Back to contents](#contents)

---  

## Technologies Used ##

### **Languages** ###

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website
- [Python3](https://www.python.org/)
  - Used to create the main application functionality

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
  - Visual Studio Code is a freeware source-code editor made by Microsoft.
- [PIP](https://pip.pypa.io/en/stable/installing/)
  - Package installer for Python. Use pip to install packages from the Python Package Index and other indexes.
- [Google Material Icons](https://fonts.google.com/icons?selected=Material+Icons)
  - Used for icons to enhance headings and add emphasis to text.
- [Google fonts](https://fonts.google.com/)
  - Used for the website fonts.
- [Color Gradient Generator](https://cssgradient.io/)
  - An online tool used to choose the website colour scheme.
- [Am I Responsive?](http://ami.responsivedesign.is/)
  - Snapshot of the responsive breakpoints of the website to visualize the look on mobile, tablet and desktop screens.
- [Adobe Illustrator](https://en.wikipedia.org/wiki/Adobe_Illustrator)
  - Adobe Illustrator is a vector graphics editor and design program developed by Adobe Inc.
- [Adobe Photoshop](https://en.wikipedia.org/wiki/Adobe_Photoshop)
  - Adobe Photoshop is a raster graphics editor developed by Adobe Inc.


[Back to contents](#contents)

---

## Features ##

### Existing Features ###

- Navbar
    - Book Icon, and Name logo. 
    - The MaterializeCSS Navbar is responsive. For small and medium screen size there is a burger icon that opens the lateral menu.

    - **For visitors** to the site who are not logged in, is available the list of all the books reviewed and the links for these pages:
        1. Books (search form)
            - Book Page (only see the detail and review of the book)
        2. Log In (form -username -password)
        3. Register (form -username -password -email)

    - **For users** who are logged in: 
        1. Books (search)
        2. Add Review (form -details of the book, Image URL and review)
        3. Profile (list of review written by the user)
            - Book Page (Edit/Delete review)
        4. Log Out    

- Python code the behaviour of the page. By checking `if 'user' in session` the user can or cannot see part of the site and functionality. Security is ensured.
- Jinja2 templating framework for Python is used to create the site's front-end dynamic content.
- If the cover image of the book is broken a `'onerror' event` handle the error displaying a dummy image.
- When you click the **Delete** button a modal window ask you to confirm or cancel the action.

- Footer
    - Show my name, and that is a link for the GitHub page of this repository.

### Back-end Design ###

- The app is created using Python3 and a Flask framework to render the HTML pages.
- The site is deployed via a Heroku app linked to a GitHub repository.
- The dynamic content is served utilising a MongoDB document based database.

### Site Construction ###

#### Topology ####
- User Logged Out, Visitor    
![Topology Logged Out](wireframe/topology-visitor.png)

- User Logged In    
![Topology Logged In](wireframe/topology-user.png)

### **Page Layout** ###

#### **Responsive Navbar** ####

- Jinja2 template conditions remove menu items based on the user logged in/out.

- **Log Out** Navbar at desktop screen sizes    
![Navbar](static/images/readme-content/navbar-logout.png)
- **Log In** Navbar at desktop screen sizes    
![Navbar](static/images/readme-content/navbar-login.png)  

- Responsive Navbar at small screen sizes    
![Mobile Navbar](static/images/readme-content/navbar-mobile.png)
- Responsive Navbar at small screen sizes, lateral menu collapsed    
![Mobile Navbar menu collapsed](static/images/readme-content/navbar-mobile-menu.png)

#### Page of the Book Reviews ####

- The book reviews page render all the cards that contain books reviewed. Available for all visitors.

- Each card contains a circular button which opens the book page with more details and the review itself.
  - When the user is the writer of the book review, another button suggest the ability to edit.

- The search bar allows the user to search through the reviews. I created a text index that allow as parameter of the search the title or author of the book.

#### Book Page ####

- The book page render the book review plus book cover image, title, author, number of pages and genre. Available for all visitors.
  - Only for the user writer of the book are visible the **Edit** and **Delete** buttons.
  - Edit button redirect to the **Edit Page**.
  - Delete button opens a confirmation modal window for the deletion.    
![Edit Review](static/images/readme-content/book-page-tablet.png)

#### Add Review Page ####

- The Add Review page consist in a form to complete and a submit button. Available only for registered user logged in.
  - the submission of the form create a new **review** item into the database.

#### Edit Review Page ####

- Only for the user writer of the book have the permission to edit the review.
  - The code search for the data of the book and pre-fills the form inputs with the current values, so that you can see exactly what you have to change.
  - Cancel button, redirect to the book reviews.
  - Submit Review button, submit all the changes.    
![Edit Review](static/images/readme-content/edit.png)

#### Register Page ####

- A new users can create an account filling the form.
  - New usernames will checked in order to be unique in the db collection.
  - Passwords are hashed before saving to the database (SHA256 Encryption with python)
 
#### Login Page ####

- Validation of both username and password, placed into users collection.

#### Profile Page ####

- The profile page displays the user's name.
- If any, Jinja will display a section that contain cards of the book reviews written by the user.
- The review button redirect the user to the book page.    
![Log In](static/images/readme-content/profile-mobile.png)

### **CRUD Functionality** ###

| Site Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Book Review |  | All book reviews |  |  |
| Book Page |  | Single book review |  | Delete single review |
| Add Review | Created book review |  |  |  |
| Edit Review |  | Single book review | Update single book review |  |
| Register | Add new user |  |  |  |
| Log In |  | User details |  |  |
| Profile |  | User details |  |  |

### User Messages ###

- Flask flash message are used to feedback user actions:
  - **Success**
  - Log In
  - Log Out
  - Register
  - Add Review
  - Edite Review
  - Delete Review
    
  - **Permission Denied**
  - Log In - username or password incorrect
  - Add Review - no session user
  - Edite Review - no session user
  - Delete Review - no session user

### Defensive Programming ###

- In order to maintain the site security, I used a defensive programming to prevent "brute force" loading of restricted pages.
  - This means that if you are not logged in, you are not able to open or see certain pages.
    - Using session cookies to validate whether a user is logged in or not.
    - Using session cookies to validate a specific user data over others data.
  - Functions in Python checks conditional statement and exception in order to handle a variety of wrong events.
    - examples of this include preventing site visitors, who aren't logged in, from just entering a page URL to bypass the login process. This type of exception redirects the user to the login page with a warning flash message.

### Additional Site features ###

- Error Handlers. Flask have a function that returns a response when a type of error is raised, in this way we can redirect the user to an Error Page, 
  that inform about the type of error, what to do or where to go. It is always present a button that redirect to the book reviews page.    

- HTTP **404** Error
- HTTP **500** Error    
- HTTP **503** Error     

![HTTP 404 Error](static/images/readme-content/error-404.png)

### **Future Features** ###

- User comments
- Email - message notification
- Upload image as a file
- Superuser

### Database Design ###

#### **users** collection ####

| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| Username | username | string |   |
| Password Hashed | password | string |   |
| Email | email | string |  |

#### **reviews** collection ####

| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| Book Title | title | String |   |
| Book Author | author | String |   |
| Number of Pages | number_pages | integer |   |
| Genre Category | genre | string |   |
| Book Review Text | review | string |   |
| Book Cover Image URL | image_url | string |   |
| Created By: User | create_by | string | username |

[Back to contents](#contents)

---

## Project Management ##

- GitHub [Projects](https://github.com/NicolaLampis/read-district/projects/1) helps to manage the planning of the website.

[Back to contents](#contents)

---

## Version Control ##
- Version control allows you to keep track of your work and helps you to easily explore the changes you have made.
- This repository is hosted by **Github** and the workspace is managed with **Gitpod**.
- Branch **Master** is the dafault branch in Git.
- To save the code development progress use the commands:
  - git add -A
  - git commit -m "your commit message"
  - git push  (default to the master branch)

#### Gitpod Workspaces ####
1. In your GitHub repository click on the Gitpod button to start the workspace.
2. Gitpod loads the **online IDE editor** window, you are ready to code.

#### Update Repository ####
- To update the repository inside GitHub, use these commands in the Gitpod terminal
  1. git add -A
  2. git commit -m "your commit message"
  3. git push  (default to the master branch)

[Back to contents](#contents)

---
## Testing ##

- Testing information can be found in a separate [testing.md](testing.md) file.

[Back to contents](#contents)

---

## Deployment ##

The website was developed using both *Gitpod* and *Visual Studio Code* and using *Git* pushed to *GitHub*, which hosts the repository. I made the following steps to deploy the site using *Heroku*:


### **Cloning the-reading-room from GitHub** ###

#### Prerequisites ####

Ensure the following are installed locally on your computer:
- [Python 3.6 or higher](https://www.python.org/download/releases/3.0/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control


#### Cloning the GitHub repository ####


- Navigate to **simonjvardy/the-reading-room**.
- Click the **Code** button.
- **Copy** the url in the dropdown box.
- Using your favourite **IDE** open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone the-reading-room:

```
git clone https://github.com/simonjvardy/the-reading-room.git
```

#### Creation of a Python Virtual Environment ####

*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html)
to understand how to create a virtual environment*

#### Install the App dependencies and external libraries ####

- In your IDE terminal window, install the dependencies from the requirements.txt file with the following command:

```
pip3 install -r requirements.txt
```

#### Create the database in MongoDB #####

*Please ensure you have an account created at [MongoDB](https://account.mongodb.com/) in order to build the database*

- In your MongoDB cluster, create a new database called `the-reading-room`
- Create the following collections within the new database:
  - [book_review](wireframes/data-schemas/book_review.json)
  - [genre](wireframes/data-schemas/genre.json)
  - [users](wireframes/data-schemas/users.json)
  - [terms_conditions](wireframes/data-schemas/terms_conditions.json)
  - [privacy](wireframes/data-schemas/privacy.json)


#### Create `env.py` file ####

- The `env.py` file should contain at least the following information:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_OWN_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_OWN_MONGODB_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_OWN_MONGODB_DATABASE_NAME")
```

- Please ensure you add in your own `SECRET_KEY`, `MONGO_URI` and `MONGO_DBNAME` values.
- ***Important:*** Add the `env.py` file to your `.gitignore` file before pushing your files to any public git repository.

#### Run the application ####

- To run the application enter the following command into the terminal window:

```
python3 app.py
```

### **Deploying The Reading Room app to Heroku** ###

#### Create the Heroku App ####

*Please ensure you have an account created at [Heroku](https://signup.heroku.com/login) in order to deploy the app*

- Log in to your Heroku account dashboard and create a new app.
- Enter the App name. 
  - This needs to be unique and the-reading-room is already in use so choose a suitable alternative name for your own App.
- Choose a geographical region closest to where you live.
  - Options available on a free account are ***United States*** or ***Europe***


#### Push your repository to GitHub ####

- Commit and push your local repository to your GitHub linked repsitory

- Ensure your local git repository has the following files in the root directory:

  - Heroku `Procfile`
  - `requirements.txt`

- If these are not showing in your local Git repository for any reason, enter the following commands in the terminal window:

```
echo web: python app.py > Procfile
pip3 freeze --local > requirements.txt
```

- Stage, commit and push your local Git repository to GitHub

#### Connect Heroku to GitHub ####

- In the Heroku App Settings page, open the section Config Vars
- Add all the environmant variables from your local `env.py` file into the Heroku Config Vars:


| Key | Value |
| --- | --- |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | YOUR_OWN_SECRET_KEY |
| MONGO_URI | YOUR_OWN_MONGODB_URI |
| MONGO_DBNAME | YOUR_OWN_MONGODB_DATABASE_NAME |


- In the Heroku App Deploy page: 
  - Select GitHub from the Deployment Method options.
  - Select Connect to GitHub.
  - Log in to your GitHub account from Heroku to link the App to GitHub.
  - Search for and select the repository to be linked in Github.
  - Select Connect.
  - Select Enable Automatic Deployment from the GitHub Master / Main branch


#### Launch the App ####

- Click Open App in Heroku to launch the App in a new browser window.



[Back to contents](#contents)

---

## Credits ##

### **Images** ###

You can find the images used for the site [here](static/images). I have sourced them through various websites, which are either free to use or used under license:

- Welcome Page
  - The Background [Hero Image](static/images/bookshelf-1920x1080.jpg) was free to use, sourced from [PIXNIO](https://pixnio.com/objects/books/bookcase-books-bookshelves-education-research-school-study) 

- Book Review


All demonstration book review image URLs were sourced from [Waterstones](https://www.waterstones.com/) online bookstore (© Waterstones, 2021. Waterstones Booksellers Limited - All Rights Reserved) from their CDN image delivery URLs and used purely for educational purposes only to demonstrate the app backend CRUD functionality. Please visit [Waterstones](https://www.waterstones.com/) for some fantastic deals on the latest books! 

  - [Silmarillion](https://cdn.waterstones.com/bookjackets/large/9780/0084/9780008433949.jpg)
  - [Clean Code: A Handbook of Agile Software Craftsmanship](https://cdn.waterstones.com/bookjackets/large/9780/1323/9780132350884.jpg)
  - [Why We Sleep: The New Science of Sleep and Dreams](https://cdn.waterstones.com/bookjackets/large/9780/1419/9780141983769.jpg)
  - [Wild: A Journey from Lost to Found](https://cdn.waterstones.com/override/v1/large/9781/7823/9781782394860.jpg)
  - [The Hunger Games - The Hunger Games 1](https://cdn.waterstones.com/bookjackets/large/9781/4071/9781407132082.jpg)
  - [White Silence - Elizabeth Cage](https://cdn.waterstones.com/bookjackets/large/9781/4722/9781472264480.jpg)
  - [The Fear Bubble: Harness Fear and Live without Limits](https://cdn.waterstones.com/bookjackets/large/9780/0081/9780008194680.jpg)
  - [Harry Potter and the Philosopher's Stone](https://cdn.waterstones.com/bookjackets/large/9781/4088/9781408855652.jpg)
  - [Gangsta Granny](https://cdn.waterstones.com/bookjackets/large/9780/0073/9780007371464.jpg)
  - [The Martian: Stranded on Mars, one astronaut fights to survive](https://cdn.waterstones.com/override/v3/large/9781/7850/9781785031137.jpg)
  - [A Promised Land](https://cdn.waterstones.com/override/v4/large/9780/2414/9780241491515.jpg)


- 404
  - The [Error 404 Text Background Image](static/images/bg.jpg) was sourced from [Colorlib](https://colorlib.com/wp/free-404-error-page-templates/) as part of a template licensed under CC BY 3.0

### **Colour** ###

- The colour palette was identified on [Coolors](https://coolors.co/)



### **Inspiration** ###

The following websites were used as the starting point and inspiration for creating the website:

- [Waterstones]() Online book store for website design inspiration and features as well as URL links to their book pages.
- [Amazon UK]() Online retailer for website design inspiration and features as well as URL links to their book pages.
- [Kirkus](https://www.kirkusreviews.com/) Book Review website / blog for design inspiration and content ideas.
- [Instagram - Duchess Of Cornwall](https://www.instagram.com/duchessofcornwallsreadingroom/?hl=en) Instagram Book Club / Book review site

























---

## Project Management ##

GitHub [Projects](https://github.com/simonjvardy/the-reading-room/projects) are used to organize the planning and development of the website.
Two GitHub projects are used to manage different aspects of the site development:
- [Development](https://github.com/simonjvardy/the-reading-room/projects/1)
  - Manages the project tasks and files.
- [Bug Fixes](https://github.com/simonjvardy/the-reading-room/projects/2)
  - Manages the triage and prioritization of the bug fixes.

The Projects are created using the following GitHub templates:
- `Automated kanban` template for the **Development** project.
- `Bug Triage` template for the **Bug Fixes** project.

The following kanban project cards are used to manage the tasks:
- **Backlog** - this card is used to capture ideas for project tasks.
- **To Do** - this is the current work queue for the project.
- **In Progress** - this is the list of tasks currently in work.
    - New issues and pull requests are automatically added to this column using project card automation options.
- **Testing** - Testing tasks list
- **Done** - completed tasks

The following Bug Triage template project cards are used to manage the Bux fixes tasks:
- **Needs Triage** - this card is used to capture new bugs prior to assigning a priority.
  - A triage card is more appropriate for larger projects than this but left in as this is where all new issues are assigned when linking a project to a new issue.
- **High Priority** - this is the high priority queue for the project.
- **Low Priority** - this is the low priority queue for the project.
- **Closed** - completed tasks.

Markdown syntax is used to create **"To-Do" list** style checkboxes by adding `- [ ]` for an un-ticked checkbox and `- [x]` for a ticked checkbox on cards as a way of splitting a single complex task into a list of steps to be completed.

![GitHub Projects - Development](static/images/github-projects-development.png)
![GitHub Projects - Bug Fixes](static/images/github-projects-bugfixes.png)


[Back to contents](#contents)

---















This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

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