import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

"""
Render the page with all the books reviewed.
Page visible to all visitors.
"""


@app.route("/")
@app.route("/get_books")
def get_books():
    """
    Reviews are ordered from the last added to the first
    into the list. If you refresh the search query you are
    safely redirected to books.html with no error.
    """
    query = request.args.get("query")
    if query:
        reviews = list(mongo.db.reviews.find(
            {"$text": {"$search": query}}).sort([("_id", -1)]))
    else:
        reviews = list(mongo.db.reviews.find().sort([("_id", -1)]))
    return render_template("books.html", reviews=reviews)


"""
Search functionality
"""


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("books.html", reviews=reviews)


"""
Registration of a new user
"""


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    New user have a unique username.
    Ensure the password is hashed.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # collect the registration form to write into the database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


"""
Log In functionality
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Sign in with username and password.
    Checks for validity of username and password entered.
    After successfully login, redirect to profile page.
    """
    if request.method == "POST":
        # check if the username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # welcome message, redirect user to the profile page
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match, redirect to login
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist, redirect to login
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


"""
User profile
"""


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    try:
        # grab the session user's username from the database
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        reviews = list(mongo.db.reviews.find({"created_by": session["user"]}))
        """
        Grant access to the user only if session cookies
        are present in the browser, otherwise redirect to login.
        """
        if session["user"]:
            return render_template(
                "profile.html", username=username, reviews=reviews)
    except Exception:
        flash("Log in first!")
        return redirect(url_for("login"))


"""
Log Out functionality
"""


@app.route("/logout")
def logout():
    # remove user from session, no cookie found
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


"""
Add a new review
"""


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    Prevents "brute force" loading of the page from any site visitor.
    If logged in the user is allowed to add a review.
    If not logged in, the user is redirected to the login page.
    """
    try:
        if session["user"]:
            if request.method == "POST":
                # collect the form data and write to MongoDB
                review = {
                    "title": request.form.get("title"),
                    "author": request.form.get("author"),
                    "cover_img": request.form.get("cover_img"),
                    "n_of_pages": request.form.get("n_of_pages"),
                    "text_review": request.form.get("text_review"),
                    "genre_name": request.form.get("genre_name"),
                    "created_by": session["user"]
                }
                mongo.db.reviews.insert_one(review)
                flash("Review Successfully Added")
                return redirect(url_for("get_books"))
            return render_template("add_review.html")
    except Exception:
        flash("Please log in first")
        return redirect(url_for("login"))


"""
Edit review functionality
"""


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Prevents "brute force" loading of the page from any site visitor.
    Only the user who wrote the review can use edit functionality.
    """
    try:
        if session["user"]:
            if request.method == "POST":
                # grab the book review details from db
                book = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
                if (session["user"] == book["created_by"]):
                    # collect the book review form data and update to MongoDB
                    submit = {
                        "title": request.form.get("title"),
                        "author": request.form.get("author"),
                        "cover_img": request.form.get("cover_img"),
                        "n_of_pages": request.form.get("n_of_pages"),
                        "text_review": request.form.get("text_review"),
                        "genre_name": request.form.get("genre_name"),
                        "created_by": session["user"]
                    }
                    mongo.db.reviews.update(
                        {"_id": ObjectId(review_id)}, submit)
                    flash("Review Successfully Updated")
                    return redirect(url_for("get_books"))
                else:
                    # this user is not the writer of the review, denied edit
                    flash("You are not allowed to edit this!")
                    return redirect(url_for("get_books"))
            review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
            return render_template("edit_review.html", review=review)
    except Exception:
        flash("Please log in first")
        return redirect(url_for("login"))


"""
Delete review functionality
"""


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    Prevents "brute force" loading of the page from any site visitor.
    Only the user who wrote the review can use delete functionality.
    """
    try:
        if session["user"]:
            mongo.db.reviews.remove({"_id": ObjectId(review_id)})
            flash("Review Successfully Deleted")
            return redirect(url_for("get_books"))
    except Exception:
        flash("Please log in first")
        return redirect(url_for("login"))


"""
Render a page with the book information and the review
"""


@app.route("/book_page/<review_id>", methods=["GET", "POST"])
def book_page(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("book_page.html", review=review)


"""
Flask error handlers, an error code trigger an HTTP response
"""


@app.errorhandler(404)
def page_not_found(error):
    """
    Error code 404 renders a error page with info for the user
    and a button that directs back to the reviews page.
    """
    return render_template("/error-handling/404.html", error=error)


@app.errorhandler(500)
def internal_server_error(error):
    """
    Error code 500 renders a error page with info for the user
    and a button that directs back to the reviews page.
    """
    return render_template("/error-handling/500.html", error=error)


@app.errorhandler(503)
def service_unavailable(error):
    """
    Error code 503 renders a error page with info for the user
    and a button that directs back to the reviews page.
    """
    return render_template("/error-handling/503.html", error=error)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
