class User:
    """
        User consists of the following Attributes:
            
            userID -> Unique 32 character string
            
            username -> Username of the User
            
            name -> Name of the User
            
            password -> Password of the User 

            city -> Name of the City User belongs to

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
                 city,
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
        pass
