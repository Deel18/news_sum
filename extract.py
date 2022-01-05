#!/usr/bin/python3
# First attempt but libraries have deprecated code that is not in use anymore.
from bs4 import BeautifulSoup
from requests import get
from requests.api import request
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

enter_url = input("Enter url for text summarization:> ")


def get_text_only(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    title = ' '.join(soup.title.stripped_strings)
    return title, text


summarize_text = get_text_only(enter_url)
print("Title : " + summarize_text[0])
print("Summary: ")
print(summarize(repr(summarize_text[1], word_count=100)))
