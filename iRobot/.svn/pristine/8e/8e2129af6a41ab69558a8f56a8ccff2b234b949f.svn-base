from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/left')
def index():
    user = { 'nickname': 'Dee' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)
