"""

Title: Prosfora : Social Media for Artists
Author: Gagan Deep Singh, Mayank Setia, Ritik Bhatnagar
Languages: Python, HTML, CSS, JavaScript, jQuery

"""
from flask import (Flask, render_template,
                   jsonify, request,
                   redirect, flash, send_file)
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_paranoid import Paranoid
from forms import (Login, Register, PictureUpload,
                   AudioUpload, VideoUpload)
from customValidators import checkForJunk
from models.user import User
from models.post import Post
from models.database import Database
from MongoLogin import *
from uuid import uuid4
from flask_login import (login_user, current_user,
                         logout_user, LoginManager,
                         login_required)
from io import BytesIO

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
    if current_user.is_authenticated:
        # TODO
        # This Code Displays posts by people being followed
        # by Current User
        pass
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/', 302)

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
            return redirect('/', 302)

    return render_template('register.html', form=form)


@app.route('/<string:username>/posts/<string:postID>')
def posts(username, postID):
    user = User.findUser(username=username)
    if not user:
        user = User.findUser(userID=username)

    if not user:
        return redirect('/'), 404, {'Refresh': '1; url = /'}

    post = Post.getPostByPostID(postID)

    if post:
        userInfo = User.toClass(User.findUser(userID=post.get('userID')))
        return render_template('post.html',
                               post=Post.to_Class(post),
                               userInfo=userInfo)

    return {'error': 'Post Not Found!'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/', 302)

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
            # print('profilePicture: ',userInfo.profilePicture)
            return render_template('profile.html', userInfo=userInfo)
        else:
            return redirect('/'), 404, {'Refresh': '1; url = /'}

    elif username is None and current_user.is_authenticated:
        return redirect(f'/profile/{current_user.username}')

    else:
        return redirect('/'), 404, {'Refresh': '1; url = /'}


@app.route("/upload", methods=['GET', 'POST'])
@app.route("/upload/picture", methods=['GET', 'POST'])
@app.route("/upload/video", methods=['GET', 'POST'])
@app.route("/upload/audio", methods=['GET', 'POST'])
@login_required
def uploadContent():
    urls = {
        "/upload": ["upload.html", None],
        "/upload/picture": ["upload_picture.html", PictureUpload, 'Picture'],
        "/upload/video": ["upload_video.html", VideoUpload, 'Video'],
        "/upload/audio": ["upload_audio.html", AudioUpload, 'Audio']
    }

    url = urls.get(request.path)[0]
    form = urls.get(request.path)[1]
    contentType = urls.get(request.path)[-1]

    if form:
        form = form()

    if request.method == 'GET':
        if url:
            return render_template(url, form=form)
        else:
            return redirect('/'), 404, {'Refresh': '1; url = /'}
    else:
        if form.validate_on_submit():

            content = form.file.data
            title = form.title.data
            description = form.description.data
            userID = current_user.userID
            postID = uuid4().hex

            if contentType == 'Audio':
                AlbumArt = form.AlbumArt.data
            else:
                AlbumArt = None

            result = User.Post(title=title,
                               content=content,
                               contentType=contentType,
                               userID=userID,
                               postID=postID,
                               description=description,
                               AlbumArt=AlbumArt)
            if result:
                return redirect(f'/{current_user.username}/posts/{postID}')
            else:
                return 'Something went wrong..'
        else:
            # print('validation failed!')
            return render_template(url, form=form)


@app.route('/data/<string:postID>.<string:ext>')
@app.route('/data/<string:AlbumArt>/<string:postID>.jpeg')
@app.route('/profile/<string:userID>/<string:profilePic>.jpeg')
@app.route('/profile/<string:userID>/<string:coverPhoto>.jpeg')
def resources(postID=None,
              userID=None,
              contentID=None,
              AlbumArt=None,
              profilePic=None,
              coverPhoto=None, 
              ext = None):

    if postID != None:
        post = Post.getPostByPostID(postID)
        if post:
            if AlbumArt:
                data = post.get('AlbumArt')
            else:
                data = post.get('content')
        else:
            flash('Unable to load Resources')
            return redirect('/'), 404, {'Refresh': '1; url = /'}
    else:
        user = User.findUser(userID=userID)
        if user:
            if profilePic:
                data = user.get('profilePic')
            else:
                data = user.get('coverPhoto')
        else:
            flash('Unable to load Resources')
            return redirect('/'), 404, {'Refresh': '1; url = /'}
        
    data = data.get('file').read()
    
    mimetype = {
        'Audio': 'audio/mpeg', 
        'Video': 'video/mp4',
        'Picture':'image/jpeg'
    }
    
    mimetype = mimetype.get(post.get('contentType'))
    
    return send_file(
        BytesIO(data),
        mimetype=mimetype,
        as_attachment=True,
        attachment_filename=f"{uuid4().hex}.jpeg")


@app.route('/profile/<string:username>/followers')
@app.route('/profile/<string:username>/following')
def followers(username=None):
    if not username:
        return redirect('/'), 404, {'Refresh': '1; url = /'}
    return render_template('followers.html')


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


if __name__ == "__main__":
    app.run(debug=True)
