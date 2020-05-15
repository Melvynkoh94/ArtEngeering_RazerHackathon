from application import app
import logging as logger
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
  logger.info("Routed to /index")
  return render_template("index.html")

@app.route("/about")
def about():
  logger.info("Routed to /about")
  return render_template("about.html")