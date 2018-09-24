from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():

 		if methods == 'GET':
					return render_template('signup_form.html')
		elif:
			methods == 'POST':
					



@app.route("")



app.run()