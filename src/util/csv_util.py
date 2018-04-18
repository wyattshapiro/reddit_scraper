import sys
import csv
import config as config

# Set encoding to utf-8 rather than ascii, as is default for python 2.
# This avoids ascii errors on csv write.
reload(sys)
sys.setdefaultencoding('utf-8')


def read_csv():
    """Reads a csv file into a list of lists
    path: String representing the path to the csv file

    return: List of Lists representing the file
    """
    input_path = config.SCRAPER_INPUT_PATH
    with open(input_path, 'rb') as f:
        reader = csv.reader(f)
        read_list = list(reader)
        return read_list[1:]


def write_row(comment=None, header=None):
    """Writes a Comment object to a csv file.

    comment: comment object to write out
    header: header row
    """
    try:
        output_path = config.SCRAPER_OUTPUT_PATH
        with open(output_path, "ab") as output:
            writer = csv.writer(output)
            if comment:
                row = [comment.subreddit_name,
                        comment.subreddit_id,
                        comment.submission_title,
                        comment.parent_comment_id,
                        comment.comment_link,
                        comment.created_utc,
                        comment.body,
                        comment.author,
                        comment.score,
                        comment.ups,
                        comment.downs,
                        comment.saved,
                        comment.gilded]
            elif header:
                row = header
            else:
                row = []
            writer.writerow(row)

    except Exception, e:
        print(e)
        print("Write row failed")
