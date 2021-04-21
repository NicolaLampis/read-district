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
  - [Responsive Design](#responsive-design)
  - [Topology](#topology)
  - [Interactive Elements](#interactive-elements)
  - [Future Features](#future-features)
  - [Site Construction](#site-construction)
  - [Page Layout](#page-layout)
  - [Construction Table](#construction-table)
  - [Database Design](#database-design)
    - [genre Collection](#genre-collection)
    - [users Collection](#users-collection)
    - [privacy Collection](#privacy-collection)
    - [terms_conditions Collection](#terms_conditions-collection)
    - [Data Types](#data-types)
- [SEO](#seo)
    - [HTML Sitemap links](#html-sitemap-links)
    - [XML Sitemap file](#xml-sitemap-file)
    - [Google Search Console](#google-search-console)
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
            - Book Page (Edit/Delete review)(Delete confirmation)
        4. Log Out    

- Python code the behaviour of the page. By checking `if 'user' in session` the user can or cannot see part of the site and functionality. Security is ensured.
- Jinja2 templating framework for Python is used to create the site's front-end dynamic content.

- Footer
    - Show my name, and that is a link for the GitHub page of this repository.

### **Back-end Design** ###

- The app is created using Python3 and a Flask framework to render the HTML pages.
- The site is deployed via a Heroku app linked to a GitHub repository.
- The dynamic content is served utilising a MongoDB document based database.

### **Site Construction** ###

#### **Topology** ####
- User Logged Out
![Topology Logged Out](wireframes/topology-user-logout.png)

- User Logged In
![Topology Logged In](wireframes/topology-user-login.png)

- Admin / Superuser Logged In
![Topology Admin User](wireframes/topology-admin-user.png)


#### **Jinja Template Relationship** ####

- Template inheritance structure: 
  ![Jinja Template layout diagram](wireframes/jinja-template-layout.png)


### **Page Layout** ###


#### **Responsive Navbar** ####

- Responsive Navbar changes at smaller screen sizes
  ![Mobile Navbar](static/images/readme-content/navbar-mobile.png)


- Navbar contains the site logo
- Jinja template conditions removes menu items based on:
  - User logged in or out
  - If the user account is Admin or Superuser

  ![Mobile navbar logged out](static/images/readme-content/navbar-mobile-logged-out.png)

  ![Mobile Navbar](static/images/readme-content/navbar-full-logged-out.png)
  
  ![Mobile navbar logged in](static/images/readme-content/navbar-mobile-logged-in.png)

  ![Mobile Navbar](static/images/readme-content/navbar-full-logged-in.png)


#### **Welcome Page** ####

- The welcome page contains a hero image utilising the Materialize CSS parallax feature
- The CTA container shows the visitor welcome message and button inviting the user to find out more.

  ![Welcome Page](static/images/readme-content/welcome-page.png)

#### **Book Review Page** ####

- The book review page shows cards containing all available book reviews
  - This page is available to all site visitors whether logged in or not.
- Each card contains a floating orange button which opens the book page for that specific book review.

- The search bar allows the user to search the available boo reviews using a text index on the book_review collection comprising the genre, author and title fields.

  ![Welcome Page](static/images/readme-content/book-review-page.png)

#### **Book Page** ####

- Shows the book review details containing the full book review details.

  ![Book Page Buttons](static/images/readme-content/book-page.png)

  - The book cover image URL is an optional field.
  - It was decided to serve a URL to a book cover image rather than saving a file for simplicity of demonstrating CRUD Functionality. However, as a future development, allowing the user to save an image file using the Flask-PyMongo `save_file()` and `send_file()` helpers is highly desirable.

- Allows the logged in users to create comments about the book review by linking t the create comment page.

  ![Comments](static/images/readme-content/book-review-comments.png)

***Book Page Buttons***

  ![Book Page Buttons](static/images/readme-content/book-page-fav-shop-btn.png)

- Favourite button
  - Writes the book ID, tile and author to the users collection as an object in the favourites array.

- Shopping Cart
  - Opens the Amazon.co.uk website showing the book as a search term in the URL.
    - Saving a new book review creates a fake Amazon.co.uk affiliate link search URL using the following format:
        `https://www.amazon.co.uk/s?k=[book]+[title]+[words]&tag=faketag`
    - This format is a compromise as it only returns a general search for the book title because specific book product page uses an Amazon ASIN product number in the URL.
    - In the case of books, the Amazon ASIN number directly matches the book's shorter ISBN-10 barcode and can link directly to the book using the minimum URL format:
        `https://www.amazon.co.uk/dp/[ASIN]`
    - However, physical copies of books primarily show the longer ISBN-13 code on the back which will not work correctly if the user records that number when creating a new book review.

- Book review edit button
  - Opens the edit review page.
  - Only available if the user created the review.

  ![Book review buttons](static/images/readme-content/book-review-buttons.png)


- Book Review delete button
  - Opens the edit review page.
  - Only available if the user created the review.

- Comments button
  - Opens the add comment page.
  - Only available to users logged in.

  ![Comments button](static/images/readme-content/comments-button.png)

#### **Add Review Page** ####

- Users who are logged in can create new book reviews by entering the book details and a book review in the add bok review form.
  - The Choose Genre select list reads data from the genres collection.
- The ADD REVIEW button submits the form data to create a new document in the book_reviews table.

  ![Add book review](static/images/readme-content/new-review.png)


#### **Edit Review Page** ####

- Only users who created the book review are permitted to edit the review.
    - Loading the page gets the current book data from the book_review collection and pre-fills the Edit Review form.

**Edit Review Buttons**
- The red cancel button returns the user to the book review page without making any changes.
- The green edit button updates the book_review document with the new data from all the form input fields.

  ![Edit book review](static/images/readme-content/edit-book-review.png)

#### **User Sign Up Page** ####

- New users are encouraged to create a new account to access more site features.
  - Usernames are required to be unique and are checked against existing usernames in the users collection.
  - The user is required to complete all fields and check-box before the new user is saved to the users collection  
  - Passwords are hashed / salted before saving to the database (SHA256)
  - The member since date and last login date are also writted automatically at this point.

  ![Sign Up](static/images/readme-content/sign-up.png)

#### **User Login Page** ####

- The user name and password are validated against existing users in the users collection.
  - Users will not be allowed to log in if either the username or password are incorrect.

  ![Log In](static/images/readme-content/log-in.png)

#### **Profile Page** ####

- The profile page displays the user's current account details.
- The Favourites section displays a summary of the user's favourite books
- The Book Reviews Written displays a summary of the user's submitted book reviews.

  ![Log In](static/images/readme-content/profile.png)

#### **Manage Genres Page** ####

- Only visible for selected users e.g. Admin or Superuser account holders.
- The page shows all current documents from the genres collection displayed in individual cards.
  - Each card has an edit and delete button for that genre document.

**Manage Genres Buttons**

- Add Genre redirects the user to the Add Genre page where a new genre category can be added
- Edit button redirects the user to the Edit Genre page where the genre name chan be updated
- Delete button deletes the genre category from the genre collection.

  ![Log In](static/images/readme-content/manage-genres.png)

#### **Add Genre Page** ####

- Allows the admin or superuser to create a new genre category
- The Add Genre button writes the genre_name to the new genre document.

  ![Log In](static/images/readme-content/add-genre.png)

#### **Edit Genre Page** ####

- Allows the admin or superuser to edit an existing genre category
    - Loading the page gets the current genre_name from the genres collection and pre-fills the Edit Genre form.

**Edit Genre Buttons**
- The red cancel button returns the user to the manage genres page without making any changes.
- The green edit button updates the genres document with the new data from the form input field.

  ![Log In](static/images/readme-content/edit-genre.png)

#### **Add Comment Page** ####
- Any user logged in can create a comment on any book review.
- The comment text, created date and username are saved as an object in the book_review table comments array.


  ![Log In](static/images/readme-content/add-comment.png)


### **CRUD Functionality** ###


| Site Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Book Review |  | All book reviews |  |  |
| Edit Review |  | Single book review | Update single book review |  |
| Book Page | Add user favourite | Single book review |  | Delete single review |
| Sign Up | Add new user |  |  |  |
| Log In |  | User details |  |  |
| Profile |  | User details |  |  |
| Profile |  | Created book reviews |  |  |
| Profile |  | Favourite reviews |  |  |
| Manage Genre |  | All genres |  | Delete genre |
| Add Genre | Add new genre |  |  |  |
| Edit Genre |  | Single genre | Update genre name |  |
| Add Comment | Add new comment |  |  |  |

### **User Alerts** ###

- Coloured Flask flash alerts are used to feedback a range of different user actions:

  - **Success**
  ![Log In](static/images/readme-content/flash-logged-in.png)
  ![Add Favourite](static/images/readme-content/flash-favourite-added.png)
  ![New Comment](static/images/readme-content/flash-new-comment.png)
  ![Review Added](static/images/readme-content/flash-review-added.png)
  ![Review Updated](static/images/readme-content/flash-review-updated.png)

  - **Advisory**
  ![Genre Deleted](static/images/readme-content/flash-genre-deleted.png)
  ![Log Out](static/images/readme-content/flash-logged-out.png)
  ![Review Deleted](static/images/readme-content/flash-review-deleted.png)


  - **Warning**
  ![Delete warning](static/images/readme-content/flash-delete-warning.png)
  ![Edit Warning](static/images/readme-content/flash-edit-warning.png)
  ![Profile Redirect](static/images/readme-content/flash-profile-redirect.png)

### **Defensive Programming** ###

- In order to try to maintain the site security, defensive programming to prevent "brute force" loading of restricted pages was introduced.
  - At its simplest level, certain pages are removed from view unless a user is logged in to the site.
    - This ustilises session cookies to validate whether a user is logged in or not.
  - The Python functions also contain checks on user input validity by employing if...esle statements as well as exception handling with try..except.
    - examples of this include preventing site visitors, who aren't logged in, from just entering a page URL to bypass the login process. This type of exception redirects the user to the login page with a warning flash message.


### **Additional Site features** ###


- A set of friendly HTTP Error landing pages for site visitors to see if a requested page is unavailable or cannot be accessed.
    - The pages provide a message to the user and a button to click to return the visitor to the homepage.

    - HTTP 404 Error
        ![HTTP 404 Error](static/images/readme-content/404-img.png)
        

    - HTTP 500 Error
        ![HTTP 500 Error](static/images/readme-content/500-img.png)

    - HTTP 503 Error
        ![HTTP 503 Error](static/images/readme-content/503-img.png)


### **Future Features** ###

- Site Admin User Account administration such as:
  - User account deactivation
  - User password change
  - moderating user comments

- Allowing users to upload image files:
  - As an alternative to a URL on book reviews
  - For a profile page thumbnail image etc.
  

### **Database Design** ###


#### [genre collection](wireframes/data-schemas/book_review.json) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Genre Name | genre_name | String |



#### [users collection](wireframes/data-schemas/users.json) ####


| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| User Name | username | string |   |
| SHA256 Hashed Password | password | String |   |
| Admin Account | is_admin | String | "off" |
| Superuser Account | is_super_user | String | "off" |
| Sign Up Date | date_joined | Date Object | utcnow() |
| Last User Login Date | last_login | Date Object | utcnow() |


#### [book_review collection](wireframes/data-schemas/book_review.json) ####


| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| Genre Category | genre | String |   |
| Book Title | title | String |   |
| Book Author | author | String |   |
| Book Cover Image URL | image_url | String |   |
| Number of Pages | number_pages | Integer |   |
| Book ISBN-13 Number | isbn | String |   |
| Book Review Text | review | String |   |
| User Book Rating | rating | String |   |
| Created By username | create_by | String | username |
| Created Date | created_date | Date Object | utcnow() |
| Updated By | mutator | String |  |
| Updated Date | mutation | Date Object |  |
| Amazon Purchase Link | purchase_link | String | "https://www.amazon.co.uk/s?k=[book]+[title]+[words]&tag=faketag" |
| Comments Array | comments | Array |   |
| Commments Array Object | text | String |   |
| Commments Array Object | created_by | String |   |
| Commments Array Object | created_date | Date Object | utcnow() |


#### [privacy collection](wireframes/data-schemas/privacy.json) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Policy Section Title | title | String |
| Section Text Array | text | Array |
| Section Text Array Object | Index | String |


#### [terms_conditions collection](wireframes/data-schemas/) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Policy Section Title | title | String |
| Section Text Array | text | Array |
| Section Text Array Object | Index | String |



#### Data Types ####

- ObjectId
- String
- Int32
- Date
- Array
- Object


[Back to contents](#contents)

---

## SEO ##

Search Engine Optimisation for the site was provided in three complementary ways:
 - HTML Sitemap links
 - XML sitemap file saved in the root directory
 - Google Search Console
 
#### HTML Sitemap links ####
- **Secondary** HTML links to each page in the website were added to the footer section of each site page to allow users an alternative means of navigating the site easily.

#### XML Sitemap file ####
- A sitemap.xml file was created to help search engines find, crawl and index the website more easily. It was created by using XML-Sitemaps.com and entering the URL for the deployed website and letting it automatically generate the required xml data for the whole site.
The file was then saved in the GitHub repository root directory.

- The following steps were used to generate the sitemap.xml file:
  1. Visit [XML-Sitemaps.com](https://www.xml-sitemaps.com/) and enter the URL of the website https://the-reading-room.herokuapp.com/
  2. Click Start
  3. The site pages will automatically be scanned 
  4. Click View Sitemap Details
  5. Download the XML sitemap file
  6. Save the sitemap.xml file in the root directory of the GitHub repository

#### Google Search Console ####
- Google Search Console was used to assist with testing and indexing issues with the website and to see how the site performs in Google search results.

- The following steps were used to perform the indexing tests:
  1.  Visit [Google Search Console](https://www.google.com/webmasters/tools/home)
  2.  Click Add Property in the menu bar
  3.  Enter the website URL https://the-reading-room.herokuapp.com/
  4.  Click Continue
  5.  Download the unique verification file created by Google
  6.  Save the [verification file](googlef750fda78af5a952.html) in the root directory of the GitHub repository
  7.  On Google Search Console, click Verify
  8.  Once the verification passes, the site is available in the Google Search Console dashboard.

Even though this website has a small number of pages and have navigation links on each page making the Sitemap largely unnecessary, I felt is was a good experience and good practice to add these features in.
Note: I haven't added a robots.txt file yet but may add this in the future when I understand more about search engine optimisation techniques.


[Back to contents](#contents)

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

## Version Control ##
**Version control** for this repository is managed within **GitHub** and **Gitpod** using separate [branches](https://github.com/simonjvardy/the-reading-room/branches)  used to work on specific aspects of the project.
The following describes the repository branch structure:
- **Master** - this is the default branch and the source for the repository deployment.
    - **Documentation** - this branch is used for updating the README.md and testing.md documentation only.
    - **Development** - this branch is used as the main working branch for the website development.
    - **Features** - this branch is used to try out new ideas and enhancements for the website.
        - Features and enhancements that are accepted are merged down into the Development branch.
    - Each individual **bug fixes** are raised within their own **separate branches** using the naming convention **\<GitHub Issue ID Number>-\<bug fix description>** e.g. branch name ***12-correct-navbar-links*** 

The following workflow steps are used to create and update branches within Gitpod and to push changes back to GitHub.


#### Gitpod Workspaces ####
1. Open **Gitpod** from **Github** using the Gitpod button. This needs to only be done **once** at the start of the project.
2. Start the Gitpod Workspace which opens an **online IDE editor** window.


#### Branches ####
3. For changes to be made to any **documentation files**, the git command `git checkout documentation` is used to checkout and switch to the **documentation branch**.
4. For changes to be made to **other files** under normal site development, the git command `git checkout development` is used to checkout and switch to the **development branch**.
5. For changes to be made to new files for site enhancements, the git command `git checkout features` is used to checkout and switch to the **features branch**.
6. To create a **new branch** for bug fixes, use the git command `git checkout -b <branch-name>` to **create and switch** to the new branch.


#### Working within a branch ####
7. **New** or **modified** files are **staged** using the `git add .` command
8. The changes are **committed** using `git commit -m "<commit message>"` command.
9. If the changes are in a newly created branch, the **committed** changes are **pushed** from Gitpod to GitHub using the `git push --set-upstream origin <branch-name>` command as there is currently no upstream branch in the remote repository.
10. For branches that have already been synchronized, the **committed** changes are **pushed** from Gitpod to GitHub using the `git push` command.


#### Merging branches in GitHub ####
11. Opening the repository in Github, a new **pull request** is created for the updated branch and assigned to its related **Development**, **Development - JavaScript** or **Bug Fixes** project.
12. The changes are **reviewed** to ensure there are **no conflicts** between the **updated branch** and the **Master branch**.
13. The changes are then **merged** into the **Master branch** and the merge request is **closed**. The **Project entry** is **automatically** moved to the **Done** card.


#### Update Gitpod with the latest GitHub commits ####
14. To update Gitpod with the **latest commits** From GitHub, the `git checkout master` command is used to checkout and switch to the master branch.
15. Use the `git pull` command to update the master branch and **reset the pointer**.
16. Now **switch** to the **other branches** in Gitpod using the `git checkout <branch-name>` command and use the `git merge origin/master` command to **update each branch in turn**.
17. Use the `git push` on **each branch** to update the relevant GiHub Branches to the **same commit** as the **Master branch**.
18. **Repeat steps 3 - 17 regularly** to ensure updates are **saved** and **correctly version controlled** in GitHub.


[Back to contents](#contents)

---
## Testing ##

- Testing information can be found in a separate [testing.md](testing.md) file.


[Back to contents](#contents)

---
## Bugs ##

To manage bugs and issues tracking, the default GitHub [bug_report.md template](https://github.com/simonjvardy/the-reading-room/blob/master/.github/ISSUE_TEMPLATE/bug_report.md) has been created and activated within the repository settings Features > Issues section.
All new bugs and issues are tracked within the GitHub repository [Issues section](https://github.com/simonjvardy/the-reading-room/issues) .
Open issues are managed within the [GitHub Projects section](https://github.com/simonjvardy/the-reading-room/projects)

Each branch is then **merged** into the **master branch** using a **pull request** that is **linked** to the **open issue**. Once merged, and the bug report **closed**, the branch is **deleted**.

Fixed bugs and issues are marked as [closed](https://github.com/simonjvardy/the-reading-room/issues?q=is%3Aissue+is%3Aclosed).


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
























### **Responsive Front-end Design** ###

- Responsive mobile first design. I used [MaterializeCSS](https://materializecss.com/) framework.
- I used [Jinja](https://jinja.palletsprojects.com/en/2.11.x/), that is a templating language for Python, modelled after Django’s templates.

### **Back-end Design** ###

- The app is created using Python3 and a Flask framework to render the HTML pages.
- The site is deployed via a Heroku app linked to a GitHub repository.
- The dynamic content is served utilising a MongoDB document based database.

### **Site Construction** ###

#### **Topology** ####
- User Logged Out
![Topology Logged Out](wireframes/topology-user-logout.png)

- User Logged In
![Topology Logged In](wireframes/topology-user-login.png)

- Admin / Superuser Logged In
![Topology Admin User](wireframes/topology-admin-user.png)


#### **Jinja Template Relationship** ####

- Template inheritance structure: 
  ![Jinja Template layout diagram](wireframes/jinja-template-layout.png)


### **Page Layout** ###


#### **Responsive Navbar** ####

- Responsive Navbar changes at smaller screen sizes
  ![Mobile Navbar](static/images/readme-content/navbar-mobile.png)


- Navbar contains the site logo
- Jinja template conditions removes menu items based on:
  - User logged in or out
  - If the user account is Admin or Superuser

  ![Mobile navbar logged out](static/images/readme-content/navbar-mobile-logged-out.png)

  ![Mobile Navbar](static/images/readme-content/navbar-full-logged-out.png)
  
  ![Mobile navbar logged in](static/images/readme-content/navbar-mobile-logged-in.png)

  ![Mobile Navbar](static/images/readme-content/navbar-full-logged-in.png)


#### **Welcome Page** ####

- The welcome page contains a hero image utilising the Materialize CSS parallax feature
- The CTA container shows the visitor welcome message and button inviting the user to find out more.

  ![Welcome Page](static/images/readme-content/welcome-page.png)

#### **Book Review Page** ####

- The book review page shows cards containing all available book reviews
  - This page is available to all site visitors whether logged in or not.
- Each card contains a floating orange button which opens the book page for that specific book review.

- The search bar allows the user to search the available boo reviews using a text index on the book_review collection comprising the genre, author and title fields.

  ![Welcome Page](static/images/readme-content/book-review-page.png)

#### **Book Page** ####

- Shows the book review details containing the full book review details.

  ![Book Page Buttons](static/images/readme-content/book-page.png)

  - The book cover image URL is an optional field.
  - It was decided to serve a URL to a book cover image rather than saving a file for simplicity of demonstrating CRUD Functionality. However, as a future development, allowing the user to save an image file using the Flask-PyMongo `save_file()` and `send_file()` helpers is highly desirable.

- Allows the logged in users to create comments about the book review by linking t the create comment page.

  ![Comments](static/images/readme-content/book-review-comments.png)

***Book Page Buttons***

  ![Book Page Buttons](static/images/readme-content/book-page-fav-shop-btn.png)

- Favourite button
  - Writes the book ID, tile and author to the users collection as an object in the favourites array.

- Shopping Cart
  - Opens the Amazon.co.uk website showing the book as a search term in the URL.
    - Saving a new book review creates a fake Amazon.co.uk affiliate link search URL using the following format:
        `https://www.amazon.co.uk/s?k=[book]+[title]+[words]&tag=faketag`
    - This format is a compromise as it only returns a general search for the book title because specific book product page uses an Amazon ASIN product number in the URL.
    - In the case of books, the Amazon ASIN number directly matches the book's shorter ISBN-10 barcode and can link directly to the book using the minimum URL format:
        `https://www.amazon.co.uk/dp/[ASIN]`
    - However, physical copies of books primarily show the longer ISBN-13 code on the back which will not work correctly if the user records that number when creating a new book review.

- Book review edit button
  - Opens the edit review page.
  - Only available if the user created the review.

  ![Book review buttons](static/images/readme-content/book-review-buttons.png)


- Book Review delete button
  - Opens the edit review page.
  - Only available if the user created the review.

- Comments button
  - Opens the add comment page.
  - Only available to users logged in.

  ![Comments button](static/images/readme-content/comments-button.png)

#### **Add Review Page** ####

- Users who are logged in can create new book reviews by entering the book details and a book review in the add bok review form.
  - The Choose Genre select list reads data from the genres collection.
- The ADD REVIEW button submits the form data to create a new document in the book_reviews table.

  ![Add book review](static/images/readme-content/new-review.png)


#### **Edit Review Page** ####

- Only users who created the book review are permitted to edit the review.
    - Loading the page gets the current book data from the book_review collection and pre-fills the Edit Review form.

**Edit Review Buttons**
- The red cancel button returns the user to the book review page without making any changes.
- The green edit button updates the book_review document with the new data from all the form input fields.

  ![Edit book review](static/images/readme-content/edit-book-review.png)

#### **User Sign Up Page** ####

- New users are encouraged to create a new account to access more site features.
  - Usernames are required to be unique and are checked against existing usernames in the users collection.
  - The user is required to complete all fields and check-box before the new user is saved to the users collection  
  - Passwords are hashed / salted before saving to the database (SHA256)
  - The member since date and last login date are also writted automatically at this point.

  ![Sign Up](static/images/readme-content/sign-up.png)

#### **User Login Page** ####

- The user name and password are validated against existing users in the users collection.
  - Users will not be allowed to log in if either the username or password are incorrect.

  ![Log In](static/images/readme-content/log-in.png)

#### **Profile Page** ####

- The profile page displays the user's current account details.
- The Favourites section displays a summary of the user's favourite books
- The Book Reviews Written displays a summary of the user's submitted book reviews.

  ![Log In](static/images/readme-content/profile.png)

#### **Manage Genres Page** ####

- Only visible for selected users e.g. Admin or Superuser account holders.
- The page shows all current documents from the genres collection displayed in individual cards.
  - Each card has an edit and delete button for that genre document.

**Manage Genres Buttons**

- Add Genre redirects the user to the Add Genre page where a new genre category can be added
- Edit button redirects the user to the Edit Genre page where the genre name chan be updated
- Delete button deletes the genre category from the genre collection.

  ![Log In](static/images/readme-content/manage-genres.png)

#### **Add Genre Page** ####

- Allows the admin or superuser to create a new genre category
- The Add Genre button writes the genre_name to the new genre document.

  ![Log In](static/images/readme-content/add-genre.png)

#### **Edit Genre Page** ####

- Allows the admin or superuser to edit an existing genre category
    - Loading the page gets the current genre_name from the genres collection and pre-fills the Edit Genre form.

**Edit Genre Buttons**
- The red cancel button returns the user to the manage genres page without making any changes.
- The green edit button updates the genres document with the new data from the form input field.

  ![Log In](static/images/readme-content/edit-genre.png)

#### **Add Comment Page** ####
- Any user logged in can create a comment on any book review.
- The comment text, created date and username are saved as an object in the book_review table comments array.


  ![Log In](static/images/readme-content/add-comment.png)


### **CRUD Functionality** ###


| Site Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Book Review |  | All book reviews |  |  |
| Edit Review |  | Single book review | Update single book review |  |
| Book Page | Add user favourite | Single book review |  | Delete single review |
| Sign Up | Add new user |  |  |  |
| Log In |  | User details |  |  |
| Profile |  | User details |  |  |
| Profile |  | Created book reviews |  |  |
| Profile |  | Favourite reviews |  |  |
| Manage Genre |  | All genres |  | Delete genre |
| Add Genre | Add new genre |  |  |  |
| Edit Genre |  | Single genre | Update genre name |  |
| Add Comment | Add new comment |  |  |  |

### **User Alerts** ###

- Coloured Flask flash alerts are used to feedback a range of different user actions:

  - **Success**
  ![Log In](static/images/readme-content/flash-logged-in.png)
  ![Add Favourite](static/images/readme-content/flash-favourite-added.png)
  ![New Comment](static/images/readme-content/flash-new-comment.png)
  ![Review Added](static/images/readme-content/flash-review-added.png)
  ![Review Updated](static/images/readme-content/flash-review-updated.png)

  - **Advisory**
  ![Genre Deleted](static/images/readme-content/flash-genre-deleted.png)
  ![Log Out](static/images/readme-content/flash-logged-out.png)
  ![Review Deleted](static/images/readme-content/flash-review-deleted.png)


  - **Warning**
  ![Delete warning](static/images/readme-content/flash-delete-warning.png)
  ![Edit Warning](static/images/readme-content/flash-edit-warning.png)
  ![Profile Redirect](static/images/readme-content/flash-profile-redirect.png)

### **Defensive Programming** ###

- In order to try to maintain the site security, defensive programming to prevent "brute force" loading of restricted pages was introduced.
  - At its simplest level, certain pages are removed from view unless a user is logged in to the site.
    - This ustilises session cookies to validate whether a user is logged in or not.
  - The Python functions also contain checks on user input validity by employing if...esle statements as well as exception handling with try..except.
    - examples of this include preventing site visitors, who aren't logged in, from just entering a page URL to bypass the login process. This type of exception redirects the user to the login page with a warning flash message.


### **Additional Site features** ###


- A set of friendly HTTP Error landing pages for site visitors to see if a requested page is unavailable or cannot be accessed.
    - The pages provide a message to the user and a button to click to return the visitor to the homepage.

    - HTTP 404 Error
        ![HTTP 404 Error](static/images/readme-content/404-img.png)
        

    - HTTP 500 Error
        ![HTTP 500 Error](static/images/readme-content/500-img.png)

    - HTTP 503 Error
        ![HTTP 503 Error](static/images/readme-content/503-img.png)


### **Future Features** ###

- Site Admin User Account administration such as:
  - User account deactivation
  - User password change
  - moderating user comments

- Allowing users to upload image files:
  - As an alternative to a URL on book reviews
  - For a profile page thumbnail image etc.
  

### **Database Design** ###


#### [genre collection](wireframes/data-schemas/book_review.json) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Genre Name | genre_name | String |



#### [users collection](wireframes/data-schemas/users.json) ####


| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| User Name | username | string |   |
| SHA256 Hashed Password | password | String |   |
| Admin Account | is_admin | String | "off" |
| Superuser Account | is_super_user | String | "off" |
| Sign Up Date | date_joined | Date Object | utcnow() |
| Last User Login Date | last_login | Date Object | utcnow() |


#### [book_review collection](wireframes/data-schemas/book_review.json) ####


| Field Description | Collection Key | Data type | Default Value |
| --- | --- | --- | --- |
| Unique ID | _id | ObjectId |   |
| Genre Category | genre | String |   |
| Book Title | title | String |   |
| Book Author | author | String |   |
| Book Cover Image URL | image_url | String |   |
| Number of Pages | number_pages | Integer |   |
| Book ISBN-13 Number | isbn | String |   |
| Book Review Text | review | String |   |
| User Book Rating | rating | String |   |
| Created By username | create_by | String | username |
| Created Date | created_date | Date Object | utcnow() |
| Updated By | mutator | String |  |
| Updated Date | mutation | Date Object |  |
| Amazon Purchase Link | purchase_link | String | "https://www.amazon.co.uk/s?k=[book]+[title]+[words]&tag=faketag" |
| Comments Array | comments | Array |   |
| Commments Array Object | text | String |   |
| Commments Array Object | created_by | String |   |
| Commments Array Object | created_date | Date Object | utcnow() |


#### [privacy collection](wireframes/data-schemas/privacy.json) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Policy Section Title | title | String |
| Section Text Array | text | Array |
| Section Text Array Object | Index | String |


#### [terms_conditions collection](wireframes/data-schemas/) ####


| Field Description | Collection Key | Data type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Policy Section Title | title | String |
| Section Text Array | text | Array |
| Section Text Array Object | Index | String |



#### Data Types ####

- ObjectId
- String
- Int32
- Date
- Array
- Object


[Back to contents](#contents)

---

## SEO ##

Search Engine Optimisation for the site was provided in three complementary ways:
 - HTML Sitemap links
 - XML sitemap file saved in the root directory
 - Google Search Console
 
#### HTML Sitemap links ####
- **Secondary** HTML links to each page in the website were added to the footer section of each site page to allow users an alternative means of navigating the site easily.

#### XML Sitemap file ####
- A sitemap.xml file was created to help search engines find, crawl and index the website more easily. It was created by using XML-Sitemaps.com and entering the URL for the deployed website and letting it automatically generate the required xml data for the whole site.
The file was then saved in the GitHub repository root directory.

- The following steps were used to generate the sitemap.xml file:
  1. Visit [XML-Sitemaps.com](https://www.xml-sitemaps.com/) and enter the URL of the website https://the-reading-room.herokuapp.com/
  2. Click Start
  3. The site pages will automatically be scanned 
  4. Click View Sitemap Details
  5. Download the XML sitemap file
  6. Save the sitemap.xml file in the root directory of the GitHub repository

#### Google Search Console ####
- Google Search Console was used to assist with testing and indexing issues with the website and to see how the site performs in Google search results.

- The following steps were used to perform the indexing tests:
  1.  Visit [Google Search Console](https://www.google.com/webmasters/tools/home)
  2.  Click Add Property in the menu bar
  3.  Enter the website URL https://the-reading-room.herokuapp.com/
  4.  Click Continue
  5.  Download the unique verification file created by Google
  6.  Save the [verification file](googlef750fda78af5a952.html) in the root directory of the GitHub repository
  7.  On Google Search Console, click Verify
  8.  Once the verification passes, the site is available in the Google Search Console dashboard.

Even though this website has a small number of pages and have navigation links on each page making the Sitemap largely unnecessary, I felt is was a good experience and good practice to add these features in.
Note: I haven't added a robots.txt file yet but may add this in the future when I understand more about search engine optimisation techniques.


[Back to contents](#contents)

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