"""
Prosfora Routes

"""
from flask import (Flask, render_template,
                   jsonify, request, session, redirect, flash)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from MongoLogin import *
from forms import Login, Register
from models.user import User
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid4())
bootstrap = Bootstrap(app)
moment = Moment(app)


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
    form = Login()
    if request.method == 'POST':
        if form.validate():
            result = User.login(form.email.data, form.password.data)
            if result is None:
                flash('Account Does not Exist!')
            elif result is False:
                flash('Invalid Password!')

            # if result is non zero
            # (True)
            # session.update(result)
            flash('Logged In!')
            session.update({'name': result.get('name')})
            return redirect('/', 302)

    return render_template('login.html', form=form)


@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/api')
def api():
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)
