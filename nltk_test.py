import urllib
import nltk
from bs4 import BeautifulSoup
from html2text import html2text
import re

#response = urllib.request.urlopen('http://python.org')
#html =response.read()
#数据清理
#soup = BeautifulSoup(html,'html.parser')
#clean =soup.get_text()
#print (clean)

#词性
from nltk import word_tokenize
s =" I was a teacher, I am watching TV"
print (nltk.pos_tag(word_tokenize(s)))

from nltk.tag.stanford import POSTagger
stan_tagger = POSTagger('/Users/wang/dev/stanford-postagger/models/english-bidirectional-distdim.tagger','/Users/wang/dev/stanford-postagger/stanford-postagger-3.9.1.jar')
tokens = word_tokenize(s)
print ('Stanord Tagger')
print (stan_tagger.tag(tokens))

#命名实体识别 NER
from nltk import ne_chunk
Sent =" Here is Stallman, he was working at HSBC Co. LTD before "
print (ne_chunk(nltk.pos_tag(word_tokenize(Sent)),binary=False))