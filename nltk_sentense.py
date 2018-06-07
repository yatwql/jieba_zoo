#分句
from nltk.tokenize import sent_tokenize
inputstring ='This is an example sent. The sentence splitter will split on sent markers. Ohh really !!'

all_sent = sent_tokenize(inputstring)
print (all_sent)

#词干抽取 stemming
from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
pst = PorterStemmer()
lst = LancasterStemmer()
print(lst.stem('eating'))
print(pst.stem('shopping'))

#词形还原 lemmatization, 此处不起作用
from nltk.stem import WordNetLemmatizer
wlem = WordNetLemmatizer()
print(wlem.lemmatize("went"))

#remove stopwords
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
text ="This is just a test"
cleanwordlist = [word for word in text.split() if word not in stoplist]
print(cleanwordlist)

