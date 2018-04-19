# Reddit Scraper

Scrape comments from given subreddits on reddit.com using PRAW

## License
Copyright (c) Wyatt Shapiro 2018

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## Installation

Clone the repo onto your machine with the following command:

$ git checkout https://github.com/wyattshapiro/reddit_scraper


## Dependencies

I used virtualenv to manage dependencies, if you have it installed you can run
the following commands from the root code directory to create the environment and
activate it:

$ virtualenv venv
$ source venv/bin/activate

Then you can run the following to install dependencies:

$ pip install -r requirements.txt

See https://virtualenv.pypa.io/en/stable/ for more information.


## Config

Create a reddit account at https://www.reddit.com/ then add username/password to src/config.py

Create a reddit app at https://www.reddit.com/prefs/apps/ and add client_id/client_secret to src/config.py

## Input

1. subreddit_name: name of subreddits

2. search_term:

- "new" for latest posts on subreddit,
- "hot" for submissions designated as hot by reddit,
- "top" for top submissions in the past submission_limit

3. submission_limit:

- for "new" or "hot" type search_term, must be int
- for "top", can be "day", "hour", "month", "week", "year", "all"

## Bugs

1. searching by "top" submissions on a subreddit returns a maximum of 100 submission results even when submission_limit = "year" or "all"

## Helpful Documentation

http://praw.readthedocs.io/en/latest/getting_started/quick_start.html
http://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
