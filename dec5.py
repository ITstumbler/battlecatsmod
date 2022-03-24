#!/usr/bin/env python
import hashlib
import sys
import os
import csv
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def decrypt(data):
    key = bytes.fromhex("313d9858a7fb939def1d7d859629087d")
    iv = bytes.fromhex("0e3743eb53bf5944d1ae7e10c2e54bdf")
    aes = AES.new(key, AES.MODE_CBC, iv)
    datas = aes.decrypt(data)
    return datas

def decrypt2(key, data):
        hexkey = hashlib.md5()
        keies = "%s"%key
        hexkey.update(keies.encode('utf-8'))
        nice = "%s"%hexkey.hexdigest()[:16]
        meet = nice.encode("latin-1")
        decrypter = AES.new(meet,AES.MODE_ECB)
        return decrypter.decrypt(data)

if len(sys.argv) != 3:
        print ("Usage: %s list-file pack-file" % sys.argv[0])
else:
        list_file = sys.argv[1]
        pack_file = sys.argv[2]
        checky = list_file.split("\\")
        check = checky[-1]
        #firstkey = "d754868de89d717fa9e7b06da45ae9e3".decode("hex")
        

        with open(list_file,'rb') as f:
                listfile = f.read()
                
        list_file_data = decrypt2('pack', listfile)

        with open(pack_file,'rb') as g:
                packfile = g.read()
                
        pack_file_data = packfile

        file_list = list_file_data.decode().split("\n")
        num_files = int(file_list[0])
        file_list = file_list[1:]
        print ("Decrypting...")

        for i in range(0, num_files):
                file_info = file_list[i].split(",")
                file_name = file_info[0]
                file_offset = int(file_info[1])
                file_size = int(file_info[2])
                file_data = pack_file_data[file_offset:file_offset+file_size]
                if check != "ImageDataLocal.list":
                    myFile = open("%s"%file_name,"wb")
                    breadfile = decrypt(file_data)
                    bytetest = breadfile[-1:]
                    if bytetest == b'\x00':
                        readfile = breadfile[:-1]
                    elif bytetest == b'\x01':
                        readfile = breadfile[:-1]
                    elif bytetest == b'\x02':
                        readfile = breadfile[:-2]
                    elif bytetest == b'\x03':
                        readfile = breadfile[:-3]
                    elif bytetest == b'\x04':
                        readfile = breadfile[:-4]
                    elif bytetest == b'\x05':
                        readfile = breadfile[:-5]
                    elif bytetest == b'\x06':
                        readfile = breadfile[:-6]
                    elif bytetest == b'\x07':
                        readfile = breadfile[:-7]
                    elif bytetest == b'\x08':
                        readfile = breadfile[:-8]
                    elif bytetest == b'\t':
                        readfile = breadfile[:-9]
                    elif bytetest == b'\n':
                        superbytetest = breadfile[-2:]
                        if superbytetest == b'\n\n':
                            readfile = breadfile[:-10]
                        else:
                            readfile = breadfile
                    elif bytetest == b'\x0b':
                        readfile = breadfile[:-11]
                    elif bytetest == b'\x0c':
                        readfile = breadfile[:-12]
                    elif bytetest == b'\r':
                        readfile = breadfile[:-13]
                    elif bytetest == b'\x0e':
                        readfile = breadfile[:-14]
                    elif bytetest == b'\x0f':
                        readfile = breadfile[:-15]
                    elif bytetest == b'\x10':
                        readfile = breadfile[:-16]
                    else:
                        readfile = breadfile
                    myFile.write(readfile)
                    myFile.close()
                else:
                    myFile = open("%s"%file_name,"wb")
                    myFile.write(file_data)
                    myFile.close()