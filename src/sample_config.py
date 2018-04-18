#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
"""
Description:
    config for the Scraper.py
"""
# your login details
username = ""
password = ""
user_agent = "crypto scraper by /u/" + username

# your reddit app details
CLIENT_ID = ""
CLIENT_SECRET = ""

# input, output setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SCRAPER_INPUT_PATH = BASE_DIR + '/src/input/input.csv'
SCRAPER_OUTPUT_PATH = BASE_DIR + "/src/output/output.csv"
