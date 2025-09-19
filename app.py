from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

  

#database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hazel123%401009@localhost/mini_system'
app.config['SQLALCHEMY_TRACT_MODIFICATION'] = False

db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(100),nullable=False, unique=True)

  


if __name__ == "__main__":
  app.run(debug=True)