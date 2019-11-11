from models.database import Database
from models.post import Post
from uuid import uuid4
from werkzeug.security import (generate_password_hash,
                               check_password_hash)
import re


class User:
    COLLECTION = 'Users'
    """
        User consists of the following Attributes:

            userID -> Unique 32 character string
            username -> Username of the User
            name -> Name of the User
            gender -> Gender of the User
            password -> Password of the User
            country -> Name of the country User belongs to
            bio -> User's Bio
            totalDownloads -> Number of Downloads of User's Content
            totalLikes -> Number of Likes of User's Content
            followers -> Array of UserIDs
            following -> Array of UserIDs
            profilePicture -> Profile Picture of the User
            coverPhoto -> Cover Photo of the User
            verified -> is User's account activated
            ProfileClicks -> Number of Profile Clicks
            currentSessions -> Array of Encrypted User ObjectID
            isPublic -> is User's profile Public
    """

    def __init__(self,
                 name,
                 username,
                 email,
                 gender,
                 userID=None,
                 password=None,
                 country=None,
                 bio="",
                 totalDownloads=0,
                 totalLikes=0,
                 followers=[],
                 following=[],
                 profilePicture=None,
                 coverPhoto=None,
                 verified=[False, None],
                 ProfileClicks=0,
                 isPublic=True,
                 totalFollowers=0,
                 totalFollowing=0,
                 _id=None,
                 currentSessions=[],
                 active=True):

        self.userID = userID
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.email = email
        self.country = country
        self.totalFollowers = totalFollowers
        self.totalFollowing = totalFollowing
        self.bio = bio
        self.totalDownloads = totalDownloads
        self.totalLikes = totalLikes
        self.followers = followers
        self.following = following
        self.profilePicture = profilePicture
        self.coverPhoto = coverPhoto
        self.verified = verified
        self.ProfileClicks = ProfileClicks
        self.isPublic = isPublic
        self.currentSessions = currentSessions
        self._id = _id
        self.active = active

    def toJson(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "username": self.username,
            "password": generate_password_hash(self.password),
            "email": self.email,
            "country": self.country,
            "bio": self.bio,
            "gender": self.gender,
            "totalDownloads": self.totalDownloads,
            "totalLikes": self.totalLikes,
            "followers": self.followers,
            "following": self.following,
            "totalFollowers": self.totalFollowers,
            "totalFollowing": self.totalFollowing,
            "profilePicture": self.profilePicture,
            "coverPhoto": self.coverPhoto,
            "verified": self.verified,
            "ProfileClicks": self.ProfileClicks,
            "currentSessions": self.currentSessions,
            "isPublic": self.isPublic
        }

    @staticmethod
    def toClass(jsonObj):
        return User(
            userID=jsonObj.get("userID"),
            name=jsonObj.get("name"),
            username=jsonObj.get("username"),
            email=jsonObj.get("email"),
            country=jsonObj.get("country"),
            bio=jsonObj.get("bio"),
            gender=jsonObj.get("gender"),
            totalDownloads=jsonObj.get("totalDownloads"),
            totalLikes=jsonObj.get("totalLikes"),
            followers=jsonObj.get("followers"),
            following=jsonObj.get("following"),
            totalFollowers=jsonObj.get("totalFollowers"),
            totalFollowing=jsonObj.get("totalFollowing"),
            profilePicture=jsonObj.get("profilePicture"),
            coverPhoto=jsonObj.get("coverPhoto"),
            verified=jsonObj.get("verified"),
            ProfileClicks=jsonObj.get("ProfileClicks"),
            currentSessions=jsonObj.get("currentSessions"),
            isPublic=jsonObj.get("isPublic"))

    def saveUser(self):
        return Database.insert(User.COLLECTION, self.toJson())

    @staticmethod
    def deleteUser(_id):
        """
        TODO
            1. Delete User's Data (POSTS)
            2. Delete All Comments made by User
            3. Delete All Replies made by User
            4. Delete entry from all users who were
               followed or being followed by user
            5. Delete All likes/dislikes made by User
            6. Delete Posts Shared by Other User
        """
        Database.delete(User.COLLECTION, {'_id': _id})

    @staticmethod
    def find(_id):
        return Database.find_one(User.COLLECTION, {'_id': _id})

    @staticmethod
    def findUser(email=None, username=None, userID=None):
        if email:
            result = Database.find_one(User.COLLECTION, {'email': email})

        elif username:
            result = Database.find_one(User.COLLECTION, {'username': username})

        elif userID:
            result = Database.find_one(User.COLLECTION, {'userID': userID})

        if result:
            return result

    @staticmethod
    def updateUserInfo(updatedUser):
        Database.update(User.COLLECTION, {
                        'userID': updatedUser.get('userID')}, updatedUser)

    @staticmethod
    def follow(cuser, user, unfollow=False):

        if unfollow:
            user.get('followers').remove(cuser.get('userID'))
            cuser.get('following').remove(user.get('userID'))
            user['totalFollowers'] = user.get('totalFollowers')-1
            cuser['totalFollowing'] = cuser.get('totalFollowing')-1
        else:
            if cuser.get('userID') not in user.get('followers'):
                user.get('followers').append(cuser.get('userID'))
                cuser.get('following').append(user.get('userID'))
                
                user['totalFollowers'] = user.get('totalFollowers')+1
                cuser['totalFollowing'] = cuser.get('totalFollowing')+1
                
        User.updateUserInfo(cuser)
        User.updateUserInfo(user)

    @staticmethod
    def login(username, password):
        isEmail = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if isEmail.fullmatch(username):
            user = User.findUser(email=username)
        else:
            user = User.findUser(username=username)

        if user:
            if check_password_hash(user.get('password'), password):
                return user
            return False

    @staticmethod
    def isUser(email=None, username=None):
        if User.findUser(email=email, username=username):
            return True
        return False

    @staticmethod
    def newsfeed(userID):
        user = User.findUser(userID=userID)
        posts = Database.find(collection=Post.COLLECTION,
                              query={"userID": {"$in": user.get('following')}})
        posts = [Post.to_Class(i) for i in posts]
        return posts

    @staticmethod
    def getFollowers(userID, following=False):
        user = User.findUser(userID=userID)
        if following:
            followers = Database.find(collection=User.COLLECTION,
                                      query={"userID": {"$in": user.get('following')}})

        else:
            followers = Database.find(collection=User.COLLECTION, query={
                                      "userID": {"$in": user.get('followers')}})

            followers = [User.toClass(i) for i in followers]

        return followers

    @staticmethod
    def checkPassword(password, email=None, username=None,):
        result = User.findUser(email, username)
        if result:
            user_password = result.get('password')
            return check_password_hash(user_password, password)
        else:
            return None

    @staticmethod
    def isVerified():
        pass

    @staticmethod
    def updateInfo():
        pass

    @staticmethod
    def updatePostInfo():
        pass

    @staticmethod
    def verifyEmail(email):
        pass

    @staticmethod
    def Post(title,
             content,
             contentType,
             userID,
             postID,
             description=None,
             AlbumArt=None):
        """
        content:
            data of the post

        type attribute for identifying :
            1. Images
            2. Videos,
            3. Audios,
        """
        post = Post(title=title,
                    content=content,
                    contentType=contentType,
                    description=description,
                    userID=userID,
                    postID=postID,
                    AlbumArt=AlbumArt)

        return post.savePost()

    @staticmethod
    def displayAllPosts(userID):
        return Post.getPostsByUserID(userID, all=True)

    @staticmethod
    def deletePost(userID, postID):
        pass

    @staticmethod
    def updatePost(postID):
        pass

    @staticmethod
    def Comment(comment, postID):
        pass

    @staticmethod
    def updateComment(comment, postID):
        pass

    @staticmethod
    def removeComment(PostID, commentID):
        pass

    @staticmethod
    def React(PostID):
        pass

    @staticmethod
    def Reply():
        pass

    @staticmethod
    def updateReply():
        pass

    @staticmethod
    def removeReply():
        pass

    @staticmethod
    def Follow():
        pass

    @staticmethod
    def Unfollow():
        pass

    @staticmethod
    def Share(postID):
        pass


if __name__ == '__main__':
    Database.initialize('Prosfora')
