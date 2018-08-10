from flask import render_template, url_for, flash, redirect
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
    return render_template('/index.html', title=title, user=user, posts=posts)

@micro.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Login'
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title=title, form=form)