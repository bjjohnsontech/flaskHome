from flask import render_template as rendTemp
from app import app


@app.route('/')
@app.route('/index')
def index():
    return rendTemp('home.html', subheader='Home')