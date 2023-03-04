from flask import Blueprint, render_template, request, flash

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
      flash('Account was created.', category="success")

  return render_template("signup.html")
