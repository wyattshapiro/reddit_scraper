# -*- coding: utf-8 -*-

import praw
import sys
import config
from models.models import Comment
import util.csv_util as csv_util

reload(sys)
sys.setdefaultencoding('utf-8')
HEADER = ["subreddit_name",
        "subreddit_id",
        "submission_title",
        "parent_comment_id",
        "comment_link",
        "created_utc",
        "body",
        "author",
        "score",
        "ups",
        "downs",
        "saved",
        "gilded"]


def get_comments(reddit, submission, comment_limit=None):
    """Get all nested comments on a submission."""
    submission = reddit.submission(id=submission)
    submission.comments.replace_more(limit=comment_limit)
    for comment in submission.comments.list():
        comment_model = Comment(comment, submission.title)
        csv_util.write_row(comment_model)


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def check_search_term(subreddit, search_term, submission_limit):
    submissions_list = []
    try:
        if search_term == "new" or search_term == "hot":
            if not ((submission_limit is None) or isinstance(submission_limit, int)):
                raise ValueError('Need to call valid submission_limit=None or int for search_term')
            elif search_term == "new":
                submissions_list = subreddit.new(limit=submission_limit)
            else:
                submissions_list = subreddit.hot(limit=submission_limit)
        elif search_term == "top":
            if (submission_limit is None):
                submission_limit = "all"
            else:
                if not isinstance(submission_limit, str):
                    raise ValueError('Need to call valid submission_limit="all" "year" "month" "week" etc for search_term')
            submissions_list = subreddit.top(time_filter=submission_limit)
        else:
            raise ValueError('Need to call valid search_term="hot", "new", or "top"')
    except Exception, e:
        print('error in check search term', e)
    finally:
        return submissions_list


def get_submissions(reddit, subreddit, search_term, submission_limit=None):
    """Get all comments inside submissions posted on subreddit."""
    try:
        i = 0
        # need to check for integer submission limit

        submissions_list = []
        submissions_list = check_search_term(subreddit, search_term, submission_limit)
        if submissions_list:
            for submission in submissions_list:
                i += 1
                print("SUBMISSION " + str(i) + " " + submission.title)
                get_comments(reddit=reddit, submission=submission)
                print("-"*50)
            return True
        else:
            raise ValueError

    except Exception, e:
        print("Error in get subreddit comments", e)
        return False


def run():
    """Scrape reddit comments for a subreddit."""
    r = praw.Reddit(client_id=config.CLIENT_ID,
                    client_secret=config.CLIENT_SECRET,
                    username=config.username,
                    password=config.password,
                    user_agent=config.user_agent)

    csv_util.write_row(comment=None, header=HEADER)

    subreddit_list = csv_util.read_csv()
    for subreddit_row in subreddit_list:
        subreddit_name = subreddit_row[0]
        search_term = subreddit_row[1]
        submission_limit = int(subreddit_row[2]) if is_int(subreddit_row[2]) else subreddit_row[2]
        subreddit = r.subreddit(subreddit_name)
        get_submissions(reddit=r, subreddit=subreddit, search_term=search_term, submission_limit=submission_limit)


if __name__ == "__main__":
    run()
