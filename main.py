from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
	return render_template('signup_form.html')

def valid_entry(data):
	if 3 < len(data) < 21 and " " not in data:
		return True
	else:
		return False

def email_check(data):
	if "@" and "." in data:
		return True
	else:
		return False


@app.route("/", methods=['POST'])
def validate_info():

	username = request.form['username']
	password1 = request.form['password1']
	password2 = request.form['password2']
	email = request.form['email']

	username_error = ''
	password1_error = ''
	password2_error= ''
	email_error = ''

	entry_error = "Error: Entry not valid. (4-20 characters with no spaces)"
	pass_error = "Error: Passwords do not match."
	email_entry_error = "Error: Not a valid email."

	if not valid_entry(username):
		username = ''
		username_error = entry_error
	if not valid_entry(password1):
		password1_error = entry_error
	if not valid_entry(password2):
		password2_error = entry_error
	if not password1 == password2:
		password1_error = pass_error
		password2_error = pass_error
	if email:
		if not email_check(email):
			email = ''
			email_error = email_entry_error
		if not valid_entry(email):
			email = ''
			email_error = entry_error

	if not username_error and not password1_error and not password2_error and not email_error:
		return render_template('signup_success.html',username=username,password1=password1,password2=password2,email=email)
	return render_template('signup_form.html',username=username,username_error=username_error,password1_error=password1_error,password2_error=password2_error,email_error=email_error,email=email)


app.run()