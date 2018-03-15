#! /usr/bin/env python
# coding=utf-8

from xml.sax.handler import ContentHandler, feature_namespaces
from xml.sax import parse, make_parser

class XmlSaxHandler(ContentHandler):
    def __init__(self, path, tag):
        try:
            super(XmlSaxHandler, self).__init__()
        except:
            ContentHandler.__init__(self)
        self.path = path
        self.tag = tag
        self.stack = []
        self.pathin = False
        self.target = False
        self.data = []
        if self.tag:
            if not self.path or not self.path[0].strip():
                self.path = [self.tag]
            else:
                self.path = self.path + [self.tag]
    def startElement(self, name, attrs):
        #print('start: ', name, attrs.keys())
        self.stack.append(name)
        self.pathin = self.judgepath(self.stack, self.path)
        if not self.tag or self.tag == name:
            self.target = True
    def endElement(self, name):
        self.stack.pop()
        if not self.tag or self.tag == name:
            self.target = False
    def characters(self, content):
        if self.pathin and self.target:
            self.data.append(content)
    def judgepath(self, stack, path):
        if not path: return True
        if len(stack) < len(path): return False
        leaf = path[0]
        if leaf not in stack: return False
        start = stack.index(leaf)
        count = stack.count(leaf)
        while count > 0:
            count -= 1
            if stack[start:] == path:
                return True
            if count > 0:
                start = stack.index(leaf, start+1)
        else:
            return False


def test(xmlfile="test.xml"):
    parser = make_parser()
    parser.setFeature(feature_namespaces, 0)

    path = ['note']
    tag = 'body'
    Handler = XmlSaxHandler(path, tag)
    parser.setContentHandler(Handler)
    try:
        parser.parse(xmlfile)
    except Exception as reason:
        print('ERROR: %s' % reason)
        exit()
    print('%s' % Handler.data)
    
if __name__ == "__main__": 
    test()
