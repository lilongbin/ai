#! /usr/bin/env python
# coding=utf-8

import jieba

try:
    input = raw_input
except:
    pass

def jiebacut(sentence):
    sentence = sentence.strip()
    if not sentence: return []
    words = [wd.strip() for wd in jieba.cut(sentence) if wd.strip()]
    return words

def test():
    sentence = input('please input a sentence: ')
    try:
        # 输出不带u的中文乱码解决
        #keywords = str(jiebacut(sentence)).decode('string_escape')
        # 输出带u的中文乱码解决
        keywords = str(jiebacut(sentence)).decode('unicode_escape')
    except AttributeError as reason:
        keywords = str(jiebacut(sentence))
    print(keywords)
    
if __name__ == '__main__':
    test()

