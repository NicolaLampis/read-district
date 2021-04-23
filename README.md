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
  - [Future Features](#future-features)
  - [Site Construction](#site-construction)
  - [Defensive Programming](#defensive-programming)
  - [Database Design](#database-design)
- [Project Management](#project-management)
- [Version Control](#version-control)
    - [Gitpod Workspaces](#gitpod-workspaces)
    - [Branches](#branches)
    - [Working within a branch](#working-within-a-branch)
    - [Merging branches in GitHub](#merging-branches-in-github)
    - [Update Gitpod with the latest GitHub commits](#update-gitpod-with-the-latest-github-commits)
- [Testing](#testing)
- [Deployment](#deployment)
  - [How To Run This Project Locally](#how-to-run-this-project-locally)  
  - [Deploy To Heroku](#deploy-to-heroku)
- [Credits](#credits)
  - [Images](#images)
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

### Additional Site features ###

- Error Handlers. Flask have a function that returns a response when a type of error is raised, in this way we can redirect the user to an Error Page, 
  that inform about the type of error, what to do or where to go. In the error page is always present a button that redirect to the book reviews page.    

- HTTP **404** Error
- HTTP **500** Error    
- HTTP **503** Error     

![HTTP 404 Error](static/images/readme-content/error-404.png)

### Future Features ###

- User comments - add a section for users interaction.
- Email - message notification of new messages.
- Upload image as a file - upload the cover image of a book.
- Superuser functionality over the site.

### Backend Design ###

- The app is created using Python3 and a Flask framework to render the HTML pages.
- The site is deployed via a Heroku app linked to a GitHub repository.
- The dynamic content is served utilising a MongoDB document based database.

### Site Construction ###

#### Topology ####
- User Logged Out, Visitor    
![Topology Logged Out](wireframe/topology-visitor.png)

- User Logged In    
![Topology Logged In](wireframe/topology-user.png)

#### Responsive Navbar ####

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

#### CRUD Functionality ####

| Site Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Book Review |  | All book reviews |  |  |
| Book Page |  | Single book review |  | Delete single review |
| Add Review | Created book review |  |  |  |
| Edit Review |  | Single book review | Update single book review |  |
| Register | Add new user |  |  |  |
| Log In |  | User details |  |  |
| Profile |  | User details |  |  |

#### User Messages ####

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
The website was developed using **Git** pushed to **GitHub**, which hosts the repository.

### How to run this project locally ###
To run this project locally you will need the following tools installed on your system:
- [Python 3.6 or higher](https://www.python.org/downloads/) and [PIP](https://pip.pypa.io/en/stable/installing/)
- An IDE such as Visual Studio Code
- Git
- An account at [MongoDB Atlas](https://www.mongodb.com)

#### Instruction ####
1. Navigate to the GitHub repository https://github.com/NicolaLampis/read-district .
    - click the Code button, then "download zip" to have a copy stored in you machine. 
        - Unzip the repository into the chosen folder, open with your favourite IDE.
    - click the Code button, copy the URL.    
        - Having Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/NicolaLampis/read-district
```
2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. Create a virtual environment with the command:
```
python -m .venv venv
```
*NOTE: Your Python command may differ, such as python3 or py*

4. Activate the **.venv** with the command:
```
.venv\Scripts\activate
```
*This command may differ depending on your operating system, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions.*

5. Install all required modules with the command:
```
pip -r requirements.txt.
```
6. Create the `env.py` file.
- In order to set the default environment variables **env.py** file should contain at least the following information:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_OWN_VALUE")
os.environ.setdefault("MONGO_URI", "YOUR_OWN_VALUE")
os.environ.setdefault("MONGO_DBNAME", "YOUR_OWN_VALUE")
```
- Replace "YOUR_OWN_VALUE" with the correct values.
- ***Important:*** Add the `env.py` file to your `.gitignore` file before pushing your files to any public git repository.
- A .gitignore file specifies intentionally untracked files that Git should ignore. In this way your sensible data remain secret and invisible.

7. You can run the application with the command:
```
python app.py
```
8. You can visit the website at http://127.0.0.1:5000

#### Create the database in MongoDB #####
- In your MongoDB cluster, create a new database called `books_db`
- Create the following collections within the new database:
  - [reviews](wireframe/data-schemas/reviews.json)  
  - [users](wireframe/data-schemas/users.json)

### Deploy to Heroku ###

1. Create a **requirements.txt** file using the terminal command `pip freeze > requirements.txt`.

2. Create a **Procfile** with the terminal command `echo web: python app.py > Procfile`.

3. Perform commands `git add` and `git commit` for both requirements and Procfile, ,then `git push` the project to GitHub.

4. Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the nearest region to you.

5. From the heroku dashboard, click on "Deploy" > "Deployment method" and select GitHub.

6. Link the heroku app to the correct GitHub repository.

7. In the heroku dashboard, click on "Settings" > "Reveal Config Vars". Insert the following KEY and VALUE:

| Key | Value |
| --- | --- |
| IP | 0.0.0.0 |
| PORT | 5000 |
| SECRET_KEY | **put_your_personal_secret_key** |
| MONGO_URI | mongodb+srv://root:**your_root_password**@myfirstcluster.iixj3.mongodb.net/**your_database_name**?retryWrites=true&w=majority |
| MONGO_DBNAME | **put_the_database_name** |

8. Select deploy branch Master.

9. Click Open App in Heroku to launch the App in a new browser window.

[Back to contents](#contents)

---

## Credits ##

### Images ###

- The cover images of the books are stored in the database as URL and are dynamically rendered in the cards.
- The source of the book images are [Wikipedia](https://www.wikipedia.org/) and [Amazon.com](https://www.amazon.com/)
- [Dummy image book](static/images/book-not-available.jpg) is hosted in unsplash.com by the artis [Fang-Wei Lin](https://unsplash.com/photos/H1IRUS1vEFA) 

### Inspiration ###

- Part of the conten for the reviews came from [Wikipedia](https://www.wikipedia.org/) and [Amazon.com](https://www.amazon.com/)

### Acknowledgements ###

- [Nicola Lampis](https://github.com/NicolaLampis) Milestone projects 1/2
- [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/) Course material, practice code challenges (Task Manager and Thorin Flask apps).
- [Simon Vardy](https://github.com/simonjvardy) for project inspiration and README.md format ideas.
- [A Greaves](https://github.com/AJGreaves) for README.md content and format ideas.
- [Rahul Nanwani](https://blog.imagekit.io/how-to-handle-loading-images-that-may-not-exist-on-your-website-92e6c3c6ea63) code inspiration on how to handle broken images.
- [Flask Documentation]() lots of resourceful content about templates, staic files and error handlers.
- [Python.org](https://python.readthedocs.io/en/latest/library/venv.html) Python VENV virtual environments documentation
- [W3Schools](https://www.w3schools.com/) amazing source of knowledge and tutorials.
- [Materialize](https://materializecss.com/) how to use components, form and javascript functionality
- [Gradient generator](https://cssgradient.io/) free tool that lets you create a gradient background for websites.