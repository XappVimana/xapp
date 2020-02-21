from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import random as random
import sys
import json
from flask_heroku import Heroku
#import secrets
#from datetime import date
#import request

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config.from_object('config')
heroku = Heroku(app)
db = SQLAlchemy(app)
#app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'


from models import Name


@app.route('/', methods=['GET','POST'])
def about():
	if request.method == 'POST':
		if 'Projects' in request.form:
			return redirect(url_for('projects'))
		elif 'Name' in request.form:
			return redirect(url_for('name'))


		return render_template('About.html')


	else:



		return render_template('About.html')

@app.route('/name', methods=['GET','POST'])
def name():
	if request.method == 'POST':
		if 'Projects' in request.form:
			return redirect(url_for('projects'))
		elif 'About' in request.form:
			return redirect(url_for('about'))

		names = request.form['name']
		n = Name(name = names)
		db.session.add(n)
		db.session.commit()

		
		'''
    	
		
		    
	    

		print('lalalal')
		details = request.form
		namez = details['name']
		namez=Names(name=namez,)
		db.session.add(namez)
		db.session.commit()
		'''






		return render_template('Names.html',name=Names.query.all())


	else:



		return render_template('Names.html',name=Names.query.all())

@app.route('/projects', methods=['GET','POST'])
def name():
	if request.method == 'POST':
		if 'Name' in request.form:
			return redirect(url_for('name'))
		elif 'About' in request.form:
			return redirect(url_for('about'))
		


		return render_template('Projects.html')


	else:
		try:
			name=Names.query.all()
		except:
			print('sss')
		#randomColor = Math.floor(random.ran t()*16777215.toString(16);
		return render_template('Projects.html')







if __name__ == '__main__':
    app.run(debug=True)


