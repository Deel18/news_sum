#!/usr/bin/python3
from newspaper import Article

article_input = input("Enter link for website:> ")
article = Article(str(article_input))

article.download()
article.parse()

# init for text sums
article.nlp()
print("Summary : ")
print(article.summary)
