#! /usr/bin/env python
# encoding=utf-8
import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

if sys.version_info[0] >= 3:
    encode_chr = str
else:
    encode_chr = unicode
HOME = os.getenv('HOME')
fhistory = HOME + os.sep + '.mycli.history'

def has_chinese_char(msg):
    for chr in msg:
        if ord(chr) > 127:
            return True
    return False

def CLI_get_line(msg='', coding='utf-8'):
    msg = encode_chr(str(msg))
    keywords = []
    if os.path.isfile(fhistory):
        with open(fhistory) as fd:
            for line in fd:
                if line[0] != '+':
                    continue
                line = line[1:].strip()
                if not line:
                    continue
                if has_chinese_char(line):
                    continue
                keywords.append(line)
    keywords = list(set(keywords))
    mycompleter = WordCompleter(keywords, ignore_case=True)
    user_input = prompt(msg,
            history=FileHistory(fhistory),
            auto_suggest=AutoSuggestFromHistory(),
            completer=mycompleter)
    return user_input.encode(coding)

def CLI_clear_history():
    if not os.path.isfile(fhistory):
        return
    with open(fhistory, 'w') as fd:
        fd.write('')
    print('%s has cleared up completed.' % os.path.basename(fhistory))

if __name__ == '__main__':
    print('%s' % CLI_get_line())

