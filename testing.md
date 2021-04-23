# Read District

[README.md file](https://github.com/NicolaLampis/read-district/blob/master/README.md)

[View the live project here.](https://read-district.herokuapp.com/)


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


During the development of this project, I had the experience of facing some problems, exhaustively testing the functionality of each part of the platform and managed to solve most of the problems that arose before writing this document.

I received help from some family and friends to do the tests on the platform resources and all the problems presented were solved without problems.

The tests were performed with a user logged in or not on the platform.

Tests of direct access to the system directly through the path without authentication or access to content restricted to another user were all blocked and worked without problems.

New agent registration tests, all existing user checks, profile options, how to change the password, change the link to the photo path and delete the account and everything worked without problems.

Tests to add new ads since all fields in the forms also responded well to the verification standards before sending the data to the server.

The request tests the data for a specific ad so that changes are made and sent back to the database also work smoothly. All error or confirmation flash messages are also running smoothly.

If you want to test a user with several properties registered for testing: Login: manoela Password: 12345

Tools used for testing
Validators
HTML

The W3C Markup Validation Service
CSS

The W3C Markup Validation Service
JavaScript

JS Hint
Python

PEP8 - The Python scripts were checked with pep8online. almost all the errors were solved, the only ones that persisted were of lines longer than 79 characters in some cases, however, in most cases they are in MongoDB query lines.
Responsiveness
The Chrome and Firefox browser development tools were used to check for responsiveness and scaling issues on different screen sizes.

This project was tested across multiple browsers (Chrome, Opera, Safari, Firefox, and IE) in different simulated and real devices.

Phones

Galaxy Note 8
Galaxy Note 9
Gakaxy Note 10 (real device)
Galaxy S5
Galaxy S7+ (real device)
Galaxy S9/S9+ (real device)
Galaxy S10 (real device)
iPhone 5/SE
iPhone 6/7/8
iPhone 8 Plus (real device)
iPhone X (real device)
iPhone XR (real device)
iphone XS
iphone XS Max (real device)
Huawei P30 Pro (real device)
Nexus 5X
Nexus 6P
Pixel 2
Pixel 2 XL
Tablets

iPad (real device)
iPad Pro 10.5-inch
iPad Pro 12.9
Kindle Fire HDX
Nexus 10
Nexus 7
Laptops

MacBook Pro 13" (real device)
Asus Swift 3 (real device)
Windows 10 computer

Philips 1080p Full HD (real device)
Were found some display issues with discontinued browsers such as IE and obsolete versions of Chrome and Opera.






Testing For User Stories Objectives
I would like the site to be easy to use.
The site is quite simple and straight forward. There are two links in the navbar for the two main sections. The add, edit and delete icons are easy to understand and use. An issue I had during testing was the feedback I had from my mentor and friends who tested the website, they found that the navbar was confusing with explanation and couldn't understand between 'My Books' and 'Books to Purchase'. To rectify this, I have replaced the name 'Books to Purchase' with 'Wishlist' and have made the necessary changes with the add form and edit form for this section as well. I have removed the add links in the navbar and placed add icons next to the page headings for the sections which will link to the add forms. This has simplifed the site and made it easy to use.

I would like to store the books that I own and want to buy on a online database.
The books are listed in a library and stored in two sections called 'My Books' and 'Wishlist' depending on if the user owns the book or wants to buy, the user can add as many books as they would like.

I would like to view the books that I have added.
Each book was stored separately in a collapsible in both the 'My Books' and 'Wishlist' sections. The header in the collapsible in the 'My Books' section, will have the book title, rating and the edit and delete icons for the book and when the collapsible is clicked, the information of the book will appear. The collapsible in the 'Wishlist' section will the same to the 'My Books' section except that in the header there will be no ratings and a third function icon link to buy will be present.

Add Book Form
Click on add book link and it will go to add book form for the 'My Books' section.
First, I will type in the book title and click the form submit button and as expected the form doesn't submit as the other required fields haven't been filled in.
Then, I also filled in the author field as well and also as expected the form didnt't submit.
Then, I filled in the third field box also which is the year the book was released and the form as expected didn't submit.
Then, I also filled in the fourth field box, the genre of the book and as expected the form didnt't submit.
Then, I filled in the book review field and submitted the form and as expected the form didnt submit.
I then filled in the last field, the rating of the book. The rating must be between zero to five so when I put in the number seven the form doesn't submit as expected as the number needs to be five or below.
When I put three in the ratings field and submit the form, as expected it submits.
The form then returns to the 'My Books' section with the book listed.
Add to Wishlist Form
Click on add to wishlist and it will go to the add to wishlist form for 'Wishlist' section.
First, I will type in the book title and click the form submit button and as expected the form doesn't submit as the other required fields haven't been filled in.
Then, I also filled in the author field as well and also as expected the form didnt't submit.
Then, I filled in the third field box also which is the year the book was released and the form as expected didn't submit.
Then, I also filled in the fourth field box, the genre of the book and as expected the form didnt't submit.
Then, I filled in the field for the reason why to buy the book and submitted the form and as expected the form didnt submit.
I then filled in the last field, the link to purchase the book and submitted the from and as expected the form submitted.
The form then returns to the 'Wishlist' section with the book listed.
Edit Book/Wishlist Entry
When I want to edit a book entry in either the 'My Books' and 'Wishlist' section, I need to click on the edit icon in the collapsible and it will take me to the edit page.
First, I will click on the edit icon in the 'My Books' section and it will take me to the edit book entry page.
Then I will change the genre from Novel to Fiction and submit the form and as expected it returns to the 'My Books' section.
I can view my change and see that it has been a success.
This will be the same experience for a edit wishlist entry.
Delete Book/Wishlist Entry
When I want to delete a book entry in either the 'My Books' and 'Wishlist' section, I need to click on the delete icon in the collapsible and it will open a confirmation modal.
First, I will click on the delete icon in the 'Wishlist' section and it will open the confirmation modal.
I will then be present with two options yes or no, I will select no, the modal will close as expected.
Then, I will again click on the delete icon and this time select yes and the modal will close.
I can now see that the book entry has been deleted
This will be the same experience as the deleting a my book entry.
Websites & Devices Testing
This site was tested on different devices such as a large desktop screen, laptop, Samsung S10+, Iphone 6/7/8, Ipad Pro and Ipad and on multiple web browsers such as Google Chrome and Firefox to make sure that it was responsive and compatible. I also had my friends and family tests it on their phones and laptops and it was responsive.

One issue I had during testing was that on a mobile screen the collapsible header was not responsive due to too much text, I resolved this by getting a materialize helper to hide the rating of the book in the header on small screen, the user can still find the rating when he clicks on the collapsible in the body.

Another minor issue that came up during testing was that when on a Galaxy Fold screen, the title would drop down from the logo, to rectify this a media query was inserted to remove the margin left.