import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db') 
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email
	
	def __repr__(self):
		return '<User %r>' % self.username

@app.route("/")
def hello():
	admin = User.query.filter_by(username='admin').first()
	return jsonify(username=admin.username,
			email=admin.email,
			id=admin.id) 

