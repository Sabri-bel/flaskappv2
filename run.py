import os #from the standard python library
# pip3 install Flask for install the framework in gitpod
# import the Flask class (capital F means class name)
# import request is for select the method
# import flash is for generate a feedback for the user -require a secret key
from flask import Flask, render_template, request, flash
import json 

#import the env library only if the env.py is found
if os.path.exists("env.py"):
    import env

# the convention requires that the instance will be stored in a variable called app
# the first argument is the name of the application module/ package
# since this is a single module, it can be used __name__ --> built in variable
# this is required because flask need to know where to look for templates and static files

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

#using the app route decorator (@ -> called decorator / way of wrapping functions)
# browse to the root directory and trigger the index function
@app.route("/") # / is for top level domain
def index():
    return render_template("index.html")


#link the about page to Flask/ also called routing 
@app.route("/about") #/about is the path
def about():
    data = []
    #this will open the file company.json as read only "r" and assign the data to the 
    #variable named json_data
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

#create a new route for each member. this app route will push the data from the member name (json file)
@app.route("/about/<member_name>")
def about_member(member_name):
    #create an empty object for storing data
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)



#we need to explict add the post method to the contact form
#by default, only get method is used with flask if not specified otherwise (error 405)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        #how to see the information entered in the debug view
        #print(request.form.get("name"))
        #print(request.form["email"])
        flash("thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact" )


@app.route("/career")
def career():
    return render_template("career.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        #if this is true, run the app with the following default arguments:
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # debug=True must be set to false in production system and before submit project 
        # this is a security flaw IMPORTANT!!!
        debug=True)