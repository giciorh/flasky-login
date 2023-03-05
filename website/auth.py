from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['post', 'get'])
def login():
  data = request.form
  print(data)
  return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
  return '<h2>Logged out</h2>'


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    firstName = request.form['firstName']
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('Email must be greater than 4 chars.', category="error")
    elif len(firstName) < 2:
      flash('Name must be greater than 2 chars.', category="error")
    elif password1 != password2:
      flash('Passwords don\'t match.', category="error")
    elif len(password1) < 8:
      flash('Password must be greater than 7 chars.', category="error")
    else:
      #add user to db
      new_user = User(email=email,
                      first_name=firstName,
                      password=generate_password_hash(password1,
                                                      method='sha256'))
      db.session.add(new_user)

      flash('Account was created.', category="success")
      return redirect(url_for('views.home'))

  return render_template("signup.html")
