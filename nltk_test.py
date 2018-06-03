import urllib
import nltk
from bs4 import BeautifulSoup
from html2text import html2text
import re

response = urllib.request.urlopen('http://python.org')
html =response.read()
soup = BeautifulSoup(html,'html.parser')
clean =soup.get_text()
print (clean)