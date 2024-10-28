from flask import Flask

"""
Create an isntance of flask  which will be  
your WSGI applicaation
"""
##WSGI application
app=Flask(__name__)  ##when I run the flask app the __name__ get striggered and the entire application runs"

@app.route("/index")  #decorator. when I vist the homepage with "/" it will call teh fucntion provided below.
def welcome():
    return "Welcome to this flask course..This is a good course."

@app.route("/homepage")  #different route to get to a different page in the flask app
def homepage():
    return "Welcome to this homepage course..This is a good course."

#Basic structure for creating a web framework using flask
if __name__ == "__main__":
    app.run(debug=True)



