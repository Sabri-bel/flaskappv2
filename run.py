import os #from the standard python library
# pip3 install Flask for install the framework in gitpod
# import the Flask class (capital F means class name)
from flask import Flask, render_template

# the convention requires that the instance will be stored in a variable called app
# the first argument is the name of the application module/ package
# since this is a singe module, it can be used __name__ --> built in variable
# this is required because flask need to know where to look for templates and static files

app = Flask(__name__)

#using the app route decorator (@ -> called decorator / way of wrapping functions)
# browse to the root directory and trigger the index function
@app.route("/") # / is for top level domain
def index():
    return render_template("index.html")


#link the about page to Flask/ also called routing 
@app.route("/about") #/about is the path
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/career")
def career():
    return render_template("career.html")


if __name__ == "__main__":
    app.run(
        #if this is true, run the app with the following default arguments:
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # debug=True must be set to false in production system and before submit project 
        # this is a security flaw IMPORTANT!!!
        debug=True)