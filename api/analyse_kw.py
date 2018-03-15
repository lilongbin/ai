#! /usr/bin/env python
# coding=utf-8

import jieba.analyse as anl

try:
    input = raw_input
except:
    pass

def get_keywords(sentence):
    sentence = sentence.strip()
    if not sentence: return []
    words = anl.extract_tags(sentence, topK=20, withWeight=True)
    return words

def test():
    fd = open(r'pinglun.txt', 'rb')
    sentence = fd.read()
    keywords = get_keywords(sentence)
    for tag, weight in keywords:
        print('%-20s %s' % (tag, weight))
    
if __name__ == '__main__':
    test()
