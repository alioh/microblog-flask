from flask import render_template
from app import micro


@micro.route('/')
@micro.route('/index')

def index():
    
    user = {'username': 'Ali'}
    title = 'Welcome to Flask'

    posts = [
        {
            'author': {'username': 'NotAli'},
            'post': 'What is Flask?'
        },
        {
            'author': {'username': 'MaybeAli'},
            'post': "I don't know what I am doing!"
        }
    ]


    return render_template('index.html', title=title, user=user, posts=posts)