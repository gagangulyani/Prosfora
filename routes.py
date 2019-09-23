"""
Prosfora Routes

"""
from flask import (Flask, render_template,
                   jsonify, request, session,
                   redirect, flash)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import functools
from MongoLogin import *
from forms import Login, Register
from models.user import User
from uuid import uuid4
from flask_login import (login_user, current_user,
                         logout_user, login_required,
                         LoginManager)
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid4())

SECRET_KEY_SESSION = None

login_manager = LoginManager()
# Added this line fixed the issue.
login_manager.init_app(app)
login_manager.login_view = 'users.login'

bootstrap = Bootstrap(app)
moment = Moment(app)
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                name=form.name.data,
                userID=str(uuid4())[::-1],
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                gender=form.gender.data
            )
            user.saveUser()
            flash('Please Login to Continue')
            return redirect('login')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global SECRET_KEY_SESSION
    form = Login()
    if request.method == 'POST':
        result = form.validate()
        if result:
            # if result is non zero
            # (True)
            # uncSession = str({'name': result.get('name')})

            # encSessionData, SECRET_KEY_SESSION = encSession(
            #     uncSession
            # )
            # print(SECRET_KEY_SESSION)
            # print(encSessionData)
            # session.update({'cu': encSessionData})
            flash(f'Hello {result.get("name")}')
            return redirect('/', 302)

    return render_template('login.html', form=form)


@app.route('/profile')
@app.route('/profile<string:username>')
def profile(username=None):
    if username:
        pass

    userInfo = {}

    return render_template('profile.html', userInfo=userInfo)


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/logout')
def logout():
    if session.get('name'):
        session.pop('name')
        flash('Logged Out Successfully!')
    return redirect('/', 302)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/api')
def api():
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
