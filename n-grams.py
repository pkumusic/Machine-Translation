from __future__ import division
from collections import defaultdict
import math

def ngrams(sentences, n):
    d = defaultdict(int)
    for sentence in sentences:
        #sentence = ['<s>'] + sentence + ['</s>']
        for i in xrange(len(sentence)-n+1):
            d[tuple(sentence[i:i+n])] += 1
    return d

def log_likelihood(sentences, unigram, bigram, alpha):
    ll = 0
    for sentence in sentences:
        prob = 1
        bigrams = [sentence[i:i+2] for i in xrange(len(sentence)-1)]
        for [w1, w2] in bigrams:
            if (w1,) in unigram:
                prob *= alpha * bigram[(w1,w2)] / unigram[(w1,)] + (1-alpha) * unigram[(w1,)]
            else:
                prob *= 10-6
        ll += math.log(prob)
    print ll

def readData(path):
    sentences = []
    with open(path, 'r') as f:
        for l in f:
            sentences.append(['<s>'] + l.strip().split(' ') + ['</s>'])
    return sentences

if __name__ == '__main__':
    data_path  = 'data/en-de/'
    train_path = data_path + 'train.en-de.en'
    valid_path  = data_path + 'valid.en-de.en'
    sentences = readData(train_path)
    valid_sentences = readData(valid_path)
    unigram = ngrams(sentences,1)
    bigram  = ngrams(sentences,2)
    log_likelihood(valid_sentences, unigram, bigram, 0.5)