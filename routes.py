from flask import Flask, render_template

app = Flask(__name__) #create instance of Flask class

@app.route("/") #map URL to python function index
	
def index(): #when user types in URL "/" index function runs and returns the index.html page
	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True) #app.run server on local server
