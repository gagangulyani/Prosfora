"""
Prosfora Routes

"""
from flask import (Flask, render_template,
                   jsonify, request,
                   redirect, flash)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_paranoid import Paranoid
from forms import Login, Register
from customValidators import checkForJunk
from models.user import User
from models.database import Database
from MongoLogin import *
from uuid import uuid4
from flask_login import (login_user, current_user,
                         logout_user, LoginManager,
                         login_required)

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid4())

# INIT DATABASE
Database.initialize('Prosfora')

# INIT Login Manager
login_manager = LoginManager()


@login_manager.user_loader
def load_user(userID):
    userObj = User.findUser(userID=userID)
    print("[FLASK-LOGIN] \nload_user()-> userID = ", userID)
    if not userObj:
        return None
    return User.toClass(userObj)


login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

bootstrap = Bootstrap(app)
moment = Moment(app)
paranoid = Paranoid(app)

paranoid.redirect_view = '/'

##################################################
# Assigning Methods to class
# [Explicitly]
##################################################
User.is_active = is_active
User.is_authenticated = is_authenticated
User.is_anonymous = is_anonymous
User.get_id = get_id
User.load_user = classmethod(load_user)


##################################################
##################################################
# ROUTES
##################################################
##################################################

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/',302)
    
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                name=form.name.data.title(),
                userID=str(uuid4())[::-1],
                username=form.username.data.lower(),
                password=form.password.data,
                email=form.email.data.lower(),
                gender=form.gender.data
            )
            user.saveUser()
            login_user(user)
            return redirect('/',302)

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/',302)

    form = Login()
    if request.method == 'POST':
        result = form.validate()
        if result:
            login_user(
                User(
                    _id=result.get('_id'),
                    name=result.get('name'),
                    userID=result.get('userID'),
                    username=result.get('username'),
                    email=result.get('email'),
                    gender=result.get('gender')
                ))
            return redirect('/', 302)

    return render_template('login.html', form=form)


@app.route('/profile')
@app.route('/profile/<string:username>')
def profile(username=None):
    userInfo = {}
    if username and not checkForJunk(
            usrtext=username) and not (len(username) > 20):
        userInfo = User.findUser(username=username)
        if userInfo:
            userInfo = User.toClass(userInfo)
            return render_template('profile.html', userInfo=userInfo)
        else:
            return 404

    elif username is None and current_user.is_authenticated:
        return redirect(f'/profile/{current_user.username}')

    else:
        return 'hi'


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/', 302)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/api')
def api():
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
