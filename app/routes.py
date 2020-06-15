from app import app
from flask import render_template,url_for



@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Mike'}
	posts = [

		{
			'author': {'username': 'john'},
			'body': 'Beautiful day in Mpls'

		},

		{
			'author': {'username': 'mike'},
			'body': 'Latest vlogs....'

		},



	]
	return render_template('index.html', title='Home', user=user, posts=posts)