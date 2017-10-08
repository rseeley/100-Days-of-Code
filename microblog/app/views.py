from flask import render_template, flash, redirect, request, abort
from flask_login import login_user
from app import app
from .models import User
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ryan'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username).first()
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')

        if not is_safe_url(next):
            return abort(400)

        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
