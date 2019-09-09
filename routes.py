"""
Prosfora Routes

"""
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/logout')
def logout():
    # displays logout page to the user
    return render_template('logout.html')

@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/api')
def api():
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
