import pandas as pd
from nltk import sent_tokenize, word_tokenize, ngrams
import nltk
import os
import string
from collections import defaultdict


def main():
    # comments = pd.read_csv('test_comments_brands.csv', names = ['polarity', 'id', 'date', 'query', 'user', 'tweet'])
    # comment_list = [sent_tokenize(sent) for sent in comments['tweet'].tolist()]
    comment_list = ['hey man how is life', 'hey man i feel good thanks what about you', 'i am doing okay', 'why just okay', 'ah you know feels man']
    entropylist = defaultdict(list)

    removals = string.punctuation + '``'
    for com in comment_list:
        ngram_statement = [str(i) for i in ngrams([iter for iter in word_tokenize(str(com)) if iter not in removals], 1)]
        counter = 0
        recent_list = []
        for gram in ngram_statement:
            gram_clean = gram[2:len(gram)-3]
            if counter == 0:
                entropylist['[start]'].append([gram_clean.lower()])
                recent_list.append([gram_clean.lower()])
            else:
                entropylist[len(recent_list)-1].append(str(gram_clean.lower()))
                recent_list.append([gram_clean.lower()])
            counter += 1

    # for x in entropylist:
    #     print x, len(entropylist[x])

    # create the conditional probability list to calculate odds based on the word
    all_entropy = {}
    for key in entropylist:
        count_vals = {}
        words_connect = len(entropylist[key])
        # print words_connect
        # print key
        for val in entropylist[key]:
            if str(val) in count_vals:
                count_vals[str(val)] += 1
            else:
                count_vals[str(val)] = 1

        cond_prob_val = {}
        for count_info in count_vals:
            cond_prob_val[count_info] = float(count_vals[count_info]) / float(words_connect)
        all_entropy[key] = [cond_prob_val]

    for x in all_entropy['[start]']:
        for y in x:
            print y, x[y]
        print '\n'
        print len(x)

main()
