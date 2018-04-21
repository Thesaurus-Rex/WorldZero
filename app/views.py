from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


# app routes
@app.route('/')
@app.route('/index')
@app.route('/login')


# definitions
def index():
    user = {'nickname': 'Molly'}
    return render_template('index.html',
                           title='home',
                           user=user)


def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
