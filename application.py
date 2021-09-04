from flask import Flask,render_template,redirect,url_for


# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.config["SECRET_KEY"] = "secretkey"


@application.route("/")
def home():
    return render_template("home.html")