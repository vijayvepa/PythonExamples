from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/user/<username>")
def displayUserName(username):
	return "Username: %s" % username
	