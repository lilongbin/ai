#! /usr/bin/env python
# coding=utf-8

import sys
from snownlp import SnowNLP

try:
    input = raw_input
except:
    pass

def get_attitude(sentence):
    sentence = sentence.strip()
    if not sentence: return []
    sentence = SnowNLP(sentence)
    #print(sentence.words)
    #print(sentence.tags)
    #print(sentence.sentiments)
    #print(sentence.keywords(3))
    #print(sentence.summary(3))
    return sentence.sentiments

def test(sentence=''):
    while not sentence.strip():
        sentence = input('please input a sentence: ')
    # if python2.x need decode to unicode
    if sys.version_info[0] == 2:
        sentence = sentence.decode("utf-8")
    try:
        # get emotional attitude
        atti = get_attitude(sentence)
    except Exception as reason:
        print('%s' % reason)
    print('The emotional attitude: %s positive' % atti)
    print('The emotional attitude: %s' % ('positive' if atti>=0.5 else 'negtive'))
    
if __name__ == '__main__':
    test()
