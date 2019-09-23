from models.database import Database
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
            isActive -> is User's account activated
            ProfileClicks -> Number of Profile Clicks
            currentSessions -> Array of Encrypted User ObjectID
            isPublic -> is User's profile Public
    """

    def __init__(self,
                 userID,
                 name,
                 username,
                 password,
                 email,
                 gender,
                 country=None,
                 bio="",
                 totalDownloads=0,
                 totalLikes=0,
                 followers=[],
                 following=[],
                 profilePicture=None,
                 coverPhoto=None,
                 isActive=[False, None],
                 ProfileClicks=0,
                 isPublic=True,
                 _id=None,
                 currentSessions=[]):

        self.userID = userID
        self.name = name
        self.username = username
        self.password = password
        self.gender = gender
        self.email = email
        self.country = country
        self.bio = bio
        self.totalDownloads = totalDownloads
        self.totalLikes = totalLikes
        self.followers = followers
        self.following = following
        self.profilePicture = profilePicture
        self.coverPhoto = coverPhoto
        self.isActive = isActive
        self.ProfileClicks = ProfileClicks
        self.isPublic = isPublic
        self.currentSessions = currentSessions
        self._id = _id

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
            "profilePicture": self.profilePicture,
            "coverPhoto": self.coverPhoto,
            "isActive": self.isActive,
            "ProfileClicks": self.ProfileClicks,
            "currentSessions": self.currentSessions,
            "isPublic": self.isPublic
        }

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
    def findUser(email=None, username=None):
        if email:
            result = Database.find_one(User.COLLECTION, {'email': email})

        if username:
            result = Database.find_one(User.COLLECTION, {'username': username})

        if result:
            return result

    @staticmethod
    def updateUserInfo(_id, updatedUserData):
        Database.update(User.COLLECTION, {'_id': _id}, updatedUserData)

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
    def createSession(_id, encryptedData):
        user = User.find(_id)
        if user:
            user.update(
                {'currentSessions': user.get('currentSessions').append(
                    encryptedData)})
            User.updateUserInfo(user.get('_id'), user)
            return True
        return False

    @staticmethod
    def findSession(session):
        pass

    @staticmethod
    def isUser(email=None, username=None):
        if User.findUser(email, username):
            return True
        return False

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
    def Post(content, type):
        """
        content:
            data of the post

        type attribute for identifying :
            1. Text,
            2. Videos,
            3. Audios,
            4. Images
        """
        pass

    @staticmethod
    def displayAllPosts(_id):
        pass

    @staticmethod
    def deletePost(postID):
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
