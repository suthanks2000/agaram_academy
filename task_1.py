from flask import Flask
from flask import render_template    #html add in python


app=Flask(__name__)

# @app.route("/welcome")
# def about():
#     return("hello")

# @app.route("/user/<name>")
# def printusername(name):
#     return name


# @app.route("/contact/<name>")  #html add in python
# def renderHTML(name):
#     return render_template("index.html",num=name)


@app.route("/list")

def rendername():
    friend=["suthan","sam","ajin"]
    return render_template("index.html",name=friend)
