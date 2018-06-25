import pandas as pd
from nltk import sent_tokenize, word_tokenize, ngrams
import nltk
import os
import string

def word_grams(words, min=1, max=4):
    s = []
    for n in range(min, max):
        for ngram in ngrams(words, n):
            s.append(' '.join(str(i) for i in ngram))
    return s

def main():
    comments = pd.read_csv('test_comments_brands.csv', names = ['polarity', 'id', 'date', 'query', 'user', 'tweet']).head(5)
    # print comments
    # comment_list = [ngrams(gram, 2) for gram in comments['tweet'].tolist()]
    comment_list = [sent_tokenize(sent) for sent in comments['tweet'].tolist()]
    # sea_text = [item for sublist in comment_list for item in sublist]
    for c in comment_list:
        ngram_statement = ' '.join(str(i) for i in ngrams([iter for iter in word_tokenize(str(c)) if iter not in string.punctuation], 3))
        print ngram_statement
        print '\n'

main()
