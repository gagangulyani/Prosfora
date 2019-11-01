from database import Database

class Reply:
    COLLECTION = 'Replies'
    """
      Reply will have the following Attributes:
      commentID -> The Comment which we are replying to
      postID -> the post which we are commenting on
      userID -> The user who is making the reply
      reply -> text responding to a comment

    """
    
    def __init__(self,
                 commentID,
                 postID,
                 userID,
                 reply):

        self.commentID = commentID
        self.postID = postID
        self.userID = userID
        self.reply = reply
        self._id = _id           

    def toJson(self):
        return {
            "commentID": self.commentID,
            "postID": self.postID,
            "userID": self.userID,
            "reply ": self.reply
        }     