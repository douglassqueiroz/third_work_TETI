# cSpell:disable
from flask import Flask, render_template, request
from random import random

app = Flask(__name__)

@app.route("/douglas")
def teti_lessons():
    return render_template("teti_douglas.html")

