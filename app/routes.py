from flask import render_template
from app import micro
from app.forms import LoginForm


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

@micro.route('/login')
def login():
    form = LoginForm()
    title = 'Login'
    return render_template('login.html', title=title, form=form)