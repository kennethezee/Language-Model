# spell checker
# Make a simple spell-checker using the ngram model. 
# This spell-checker should go through a document and find all spelling errors. 

import re
import nltk
import numpy as np
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

# read words from text file
file = open('wrong_spelling.txt','r')
doc = file.read()
# tokenize the words
word_tokens = word_tokenize(doc)
wrong = []
for words in word_tokens:
    r = re.sub("[.,']", "", words)
    wrong.append(r)
    for wordss in wrong:
        if wordss == "":
            wrong.remove(wordss)

file2 = open('right_spelling.txt','r')
doc2 = file2.read()
# tokenize the words
right_word_tokens = word_tokenize(doc2)
right = []
for words in right_word_tokens:
    r = re.sub("[.,']", "", words)
    right.append(r)
    for wordss in right:
        if wordss == "":
            right.remove(wordss)
            
for wr in right:
    if wr in stopwords or wr == "I":
        right.remove(wr)

for ws in wrong:
    if ws in stopwords or ws == "I":
        wrong.remove(ws)

from nltk.tokenize import sent_tokenize
wls = sent_tokenize(doc)

from nltk.util import ngrams
bigrams = list(ngrams(wrong, 2))
bigrams_right = list(ngrams(right, 2))

fdist = FreqDist(wrong)

for word in bigrams:
    if word not in bigrams_right:
        continue
    for w in word:
        if w in right:
            fdist[word] += 1
        
misspelled = []
def spell_checker(bigrams):
    for gram in bigrams:
        prob = fdist[(gram)] / fdist[(gram[0])]
        if prob == 0.0:
            print(str(gram) + " there is misspelling here, please look over your sentence.")
            misspelled.append(gram)

spell_checker(bigrams)



