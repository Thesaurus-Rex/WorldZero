from app import app
from flask import render_template


@app.route('/')
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