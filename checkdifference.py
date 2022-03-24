#!/usr/bin/env python
import hashlib
import sys
from Crypto.Cipher import AES
import os
import csv
import itertools

def encrypt(key, data):
        hexkey = hashlib.md5()
        keies = "%s"%key
        hexkey.update(keies.encode('utf-8'))
        nice = "%s"%hexkey.hexdigest()[:16]
        meet = nice.encode("latin-1")
        encrypter = AES.new(meet,AES.MODE_ECB)
        return encrypter.encrypt(data)

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

if len(sys.argv) != 3:
        print ("Usage: %s folder-name" % sys.argv[0])
else:
        oldfoldername = sys.argv[1]
        newfoldername = sys.argv[2]
        for filename in os.listdir(oldfoldername):
            with open("%s\\%s" % (oldfoldername, filename),"rb") as file:
                readfile = file.read()
                vars()[filename] = readfile
        for filename in os.listdir(newfoldername):
            with open("%s\\%s" % (newfoldername, filename),"rb") as file:
                readfile = file.read()
                fileboner = filename + "1"
                vars()[fileboner] = readfile
                try:
                  vars()[filename]
                except KeyError:
                  kek = 1
                else:
                    if vars()[fileboner] != vars()[filename]:
                        print(filename)