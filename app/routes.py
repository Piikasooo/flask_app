from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Artem'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Beautiful day in Kiev!'
        },
        {
            'author': {'username': 'Karl'},
            'body': 'The Halk movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home',
                           user=user, posts=posts)