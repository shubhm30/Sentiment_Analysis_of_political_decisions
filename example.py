import re
import csv
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
#from nltk.stem.snowball import EnglishStemmer
from nltk.stem.wordnet import WordNetLemmatizer


def rem_stpwords(sen):
    exp = r'\w+'
    tokenizer = RegexpTokenizer(exp)
    token = tokenizer.tokenize(sen)
    words = [w for w in token if not w in stopwords.words('english')]
    return " ".join(words)

# def stem_words(sentence):
#     stemmer = EnglishStemmer()
#     exp = r'\w+'
#     tokenizer = RegexpTokenizer(exp)
#     token = tokenizer.tokenize(sentence)
#     words = [stemmer.stem(w) for w in token ]
#     return " ".join(words)


def lemm_words(sentence):
    lemm = WordNetLemmatizer()
    exp = r'\w+'
    tokenizer = RegexpTokenizer(exp)
    token = tokenizer.tokenize(sentence)
    words = [lemm.lemmatize(w) for w in token ]
    return " ".join(words)

row = "RT @shubham: NCERT to review expert working in schools 21321 323 textbooks to update 3283823 11content; may include #demonetisation #GST https://t.co/Ea9JZIKepE"
row = row.lower()  # converts text to lowercase
st_ht = re.sub(r'#', "", row)  # remove hashtags
st_at = re.sub(r'@\w+', "", st_ht)  # removes @user
st_rt = re.sub(r'\brt\b', "", st_at)  # removes RT
st_url = re.sub(r'(?:\@|https?\://)\S+', "", st_rt)    # removes URLs
st_num = re.sub(r'\d+', "", st_url)     # removes digits
st_stp = rem_stpwords(st_num)
st = lemm_words(st_stp)
print(st)
