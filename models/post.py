from database import Database


class Post:
    COLLECTION = 'Posts'
    """
        Post consists of the following Attributes:

            postID -> Unique 32 character string
            userID -> Unique 32 character string
            contentType -> Choose from Multiple Media Options
            title -> Title of the Post/Track Name/Video Name
            content -> Written Content of the Post
            description -> Explanation of files chosen for upload
            comments -> Array of commentID's
            totalLikes -> Number of likes on the Post Made
            totalDownloads -> Number of Downloads made of the PostContent
            totalClicks -> No of Clicks which will be used for Trending Section
            likes -> List of User's who have liked the Post
            dislikes -> List of User's who disliked the Post
            _id -> Unique ID Assigned by MongoDB

    """

    def __init__(self,
                 postID,
                 userID,
                 contentType,
                 title,
                 content,
                 description,
                 comments=[],
                 totalLikes=0,
                 totalDownloads=0,
                 totalClicks=0,
                 likes=[],
                 dislikes=[],
                 _id=None):

        self.postID = postID
        self.userID = userID
        self.contentType = contentType
        self.title = title
        self.content = content
        self.description = description
        self.comments = comments
        self.totalLikes = totalLikes
        self.totalDownloads = totalDownloads
        self.totalClicks = totalClicks
        self.likes = likes
        self.dislikes = dislikes
        self._id = _id

    def toJson(self):
        return {
            "postID": self.postID,
            "userID": self.userID,
            "contentType": self.contentType,
            "title": self.title,
            "content": self.content,
            "description": self.description,
            "comments": self.comments,
            "totalLikes": self.totalLikes,
            "totalDownloads":self.totalDownloads,
            "totalClicks": self.totalClicks,
            "likes": self.likes,
            "dislikes": self.dislikes
        }

    @staticmethod
    def to_Class(json_):
        return User(
            "postID": json_.postID,
            "userID": json_.userID,
            "contentType": json_.contentType,
            "title": json_.title,
            "content": json_.content,
            "description": json_.description,
            "comments": json_.comments,
            "totalLikes": json_.totalLikes,
            "totalDownloads":json_.totalDownloads,
            "totalClicks": json_.totalClicks,
            "likes": json_.likes,
            "dislikes": json_.dislikes
        )
    @staticmethod
    def savePost(self):
        """
        Saves Post into Database
        *Uses gridFS for storing binary data seperately for easy access
        """
        self.content = Database.saveFile(self.content)
        return Database.insert(Post.COLLECTION, self.toJson())

    @staticmethod
    def updatePost(self):
        pass

    @staticmethod
    def deletePost(self):
        pass

    @staticmethod
    def viewLikes(self):
        pass

    @staticmethod
    def viewComments(self):
        pass
