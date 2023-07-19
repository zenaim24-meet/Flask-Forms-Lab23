from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

usernames= { "siwarha": "123", "zenaim": "456", "zainab":"789"}
username = "siwarha"
password = "123"
facebook_friends=["layan","karmel","sally", "dara", "amar", "kinzi"]


@app.route('/', methods= ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name=request.form['username']
		pass1=request.form['password']
		if name in usernames and usernames[name]==pass1:
			return redirect(url_for('welcome'))
		else: 
			return render_template('login.html')

  
@app.route('/home', methods=['GET','POST'])
def welcome():
	return render_template('home.html', friends= facebook_friends)





@app.route('/friend_exists/<string:name>')
def hi(name):
	return render_template('friend_exists.html', st= name in facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
