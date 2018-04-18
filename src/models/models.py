class Comment(object):
    """Object which represents a Reddit comment whose info we are going to scrape."""
    def __init__(self, comment, submission_title):
        """sets values based on response from reddit api"""

        self.subreddit_name = comment.subreddit_name_prefixed
        self.subreddit_id = comment.subreddit_id
        self.submission_title = submission_title
        self.parent_comment_id = comment.parent_id
        self.comment_link = comment.permalink
        self.created_utc = comment.created_utc
        self.body = comment.body
        self.author = "n/a" if (comment.body == '[removed]' or comment.body == '[deleted]' or comment.author is None) else comment.author.name
        self.ups = comment.ups
        self.downs = comment.downs
        self.saved = comment.saved
        self.score = comment.score
        self.score_hidden = comment.score_hidden
        self.gilded = comment.gilded
        self.success = True

    def get_success(self):
        """Helper method to get success"""
        return self.success

        # data type
        # self.body = ""
        # self.subreddit_name = ""
        # self.subreddit_id = ""
        # self.comment_link = ""
        # self.parent_id = ""
        # self.created_utc = None
        # self.author = ""
        # self.ups = 0
        # self.downs = 0
        # self.saved = False
        # self.score = 0
        # self.score_hidden = False
        # self.gilded = 0
        # self.success = False
