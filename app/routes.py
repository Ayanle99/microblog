from app import app
from flask import render_template,url_for, flash, redirect
from app.forms import LoginForm 


@app.route('/about')
def about():
	return render_template('about.html')



@app.route('/java')
def java():
	return render_template('java.html', title='Java')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		flash("login successful", 'success')
		return redirect('/index')

	return render_template('login.html', title='Login', form=form)

@app.route('/')
@app.route('/home')
def home():
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
	return render_template('home.html', title='Home', user=user, posts=posts)




if __name__ == '__main__':
    app.run(debug=True)