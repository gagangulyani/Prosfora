from database import Database 

class Comment:
    COLLECTION= 'Comments'
    """
      Comment consists of the following Attributes:

          commentID -> Unique 32 Character String
          postID -> The Post on which comment/Feedback is provided
          userID -> The User who has made the comment
          commentText -> Text/feedback given 
    """

    def __init__(self,
                 commentID,
                 postID,
                 userID,
                 commentText,
                 _id):

        self.commentID = commentID
        self.postID = postID
        self.userID = userID
        self.commentText = commentText
        self._id = _id

    def toJson(self):
        return {
            "commentID": self.commentID,
            "postID": self.postID,
            "userID": self.userID,
            "commentText" self.commentText
        }    

    @staticmethod
    def view
