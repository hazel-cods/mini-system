from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/message")
def message():
  return render_template("message.html")





if __name__ == "__main__":
  app.run(debug=True)