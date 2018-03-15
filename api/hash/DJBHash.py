#! /usr/bin/env python
# coding=utf-8

def DJBHash(sstr):
     hash = 5381
     for i in range(len(sstr)):
         hash = ((hash << 5) + hash) + ord(sstr[i])
     return hash

def hash_test(sstr):
    hash = DJBHash(sstr)
    print("hash: %s" % hash)
def main():
    while True:
        sstr = raw_input('$ ')
        if not sstr.strip():
            break
        hash_test(sstr)

if __name__ == "__main__":
    main()

