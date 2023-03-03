from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
  return '<h2>Login</h2>'


@auth.route('/logout')
def logout():
  return '<h2>Logout</h2>'


@auth.route('/signup')
def signup():
  return '<h2>Sign Up</h2>'
