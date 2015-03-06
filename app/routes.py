from flask import render_template as rendTemp
from app import app
from app.views import headers

@app.route('/')
@app.route('/index')
def index():
    return rendTemp('home.html', header=headers.home())

@app.route('/profile')
def profile():
    return rendTemp('profile.html', header=headers.profile(), css='<link rel="stylesheet" href="static/css/tree.css">')

@app.route('/portfolio')
def port():
    return rendTemp('portfolio.html', header=headers.portfolio())

@app.route('/certs')
def certs():
    return rendTemp('certs.html', header=headers.certs())