from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

  

#database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hazel123%401009@localhost/mini_system'
app.config['SQLALCHEMY_TRACT_MODIFICATION'] = False



@app.route("/")
def index():
  return render_template("index.html")

@app.route("/message")
def message():
  return render_template("message.html")




if __name__ == "__main__":
  app.run(debug=True)