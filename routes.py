"""
Prosfora Routes

"""
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms import LoginForm, Join


app = Flask(__name__)
app.config['SECRET_KEY']='05b714016e2cf744e1aac4d021404a72'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm() 
    return render_template('login.html',form=form)


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
