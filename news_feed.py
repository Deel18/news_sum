#!/usr/bin/python3
import os
import requests
import json
import time
import argparse

API_KEY = os.getenv("API_KEY")


parser = argparse.ArgumentParser(description='News feed.')
parser.add_argument("-sw", "--search_word", nargs='+',
                    help='Enter search term for news.')
parser.add_argument("-hl", "--headlines", nargs='+',
                    help="Fetch headlines for entered country.")
args = parser.parse_args()


if args.search_word:
    url = (
        f'https://newsapi.org/v2/everything?q={args.search_word[0]}&apiKey={API_KEY}')
    try:
        response = requests.get(url)
    except:
        print("Unable to fetch information.")

    news = json.loads(response.text)

    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']))
        print(str(new['url']), "\n\n")
        print('______________________________________________________\n')
        print(str(new['description']), "\n\n")
        print("..............................................................")
        time.sleep(20)

elif args.headlines:
    url = (
        f'https://newsapi.org/v2/top-headlines?country={args.headlines[0]}&apiKey={API_KEY}')

    try:
        response = requests.get(url)
    except:
        print("Unable to fetch information.")

    news = json.loads(response.text)

    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']))
        print(str(new['url']), "\n\n")
        print('______________________________________________________\n')
        print(str(new['description']), "\n\n")
        print("..............................................................")
        time.sleep(20)
