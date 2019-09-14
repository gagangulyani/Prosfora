from database import Database

class User:
    COLLECTION = 'Users'
    """
        User consists of the following Attributes:

            userID -> Unique 32 character string

            username -> Username of the User

            name -> Name of the User

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

            isPublic -> is User's profile Public

    """

    def __init__(self,
                 userID,
                 name,
                 username,
                 password,
                 email,
                 country,
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
                 _id=None):

        self.userID = userID
        self.name = name
        self.username = username
        self.password = password
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
        self._id = _id

    def toJson(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "country": self.country,
            "bio": self.bio,
            "totalDownloads": self.totalDownloads,
            "totalLikes": self.totalLikes,
            "followers": self.followers,
            "following": self.following,
            "profilePicture": self.profilePicture,
            "coverPhoto": self.coverPhoto,
            "isActive": self.isActive,
            "ProfileClicks": self.ProfileClicks,
            "isPublic": self.isPublic
        }

    @staticmethod
    def saveUser(usrObj):
        Database.insert(User.COLLECTION, usrObj)

    @staticmethod
    def findUser(_id):
        return Database.find(User.COLLECTION, {'_id': _id})

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
        """
        Database.delete(User.COLLECTION, {'_id': _id})

    @staticmethod
    def 




if __name__ == '__main__':
    Database.initialize('Prosfora')


