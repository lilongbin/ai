#! /usr/bin/env python
# coding=utf-8

class HashMap(object):
    def __init__(self, tablen):
        self.tablen = tablen
        self.hashtab = [None,]*self.tablen
    def hashcode(self, sstr):
         hash = 5381
         for i in range(len(sstr)):
             hash = ((hash << 5) + hash) + ord(sstr[i])
         return hash
    def indexfor(self, hash):
        return hash % self.tablen
    def put(self, k, v):
        hindex = self.indexfor(self.hashcode(k))
        print("put: <%s, %s>" % (k, v))
        if not self.hashtab[hindex]:
            #print('add %s' % v)
            self.hashtab[hindex] = [v,]
        else:
            if v in self.hashtab[hindex]:
                return
            #print('append %s' % v)
            self.hashtab[hindex].append(v)
    def get(self, k):
        hindex = self.indexfor(self.hashcode(k))
        v = self.hashtab[hindex]
        print("get: %s->%s" % (hindex, v))
        return v

def hash_test():
    hm = HashMap(10)
    while True:
        k = raw_input('key: ').strip()
        if not k:
            break
        v = raw_input('value: ').strip()
        if not v:
            break
        hm.put(k, v)
        hm.get(k)

def main():
    hash_test()
    
if __name__ == "__main__":
    main()

