from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')


@app.route('/login')
def login():
    form =  LoginForm()
    return render_template('login.html', title='Sign In', form = form)


@app.route('/index')
def index():
    user = {'username': 'pixie'}
    tasks = [
        {
            'author':{'username': 'Loki'},
            'body': 'I did something tricky!'
        },
        {
            'author': {'username': 'Bex'},
            'body': 'I did something heroic!'
        }

    ]
    return render_template('index.html', title = 'Home', user = user, tasks = tasks)
