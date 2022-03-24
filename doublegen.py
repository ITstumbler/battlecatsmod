#!/usr/bin/env python
import hashlib
import sys
from Crypto.Cipher import AES
import os
import csv
import itertools

def encrypt(data):
    key = bytes.fromhex("d754868de89d717fa9e7b06da45ae9e3")
    iv = bytes.fromhex("40b2131a9f388ad4e5002a98118f6128")
    aes = AES.new(key, AES.MODE_CBC, iv)
    datas = aes.encrypt(data)
    return datas

def encrypt2(key, data):
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
        path = sys.argv[1]
        foldername = sys.argv[2]
        dotruebytes = 0
        removebytes = 0
        ptruebytes = 0
        #sortedpath = sorted(os.listdir(path), key=lambda s: s.casefold())
        sortedpath = sorted(os.listdir(path))
        fileoffset = 0
        totalfile = 0
        listfileplain = ""
        packfileplain = ""
        print ("Generating list & pack files...")
        for filename in sortedpath:
            totalfile += 1
        listfile = open("temp.list","w")
        listfile.write(str(totalfile))
        listfile.write(chr(0x0a))           
        rawpackfile = open("temp.pack","wb+")
        for filename in sortedpath:
            with open("%s/%s" % (path, filename),"rb") as file:
                if foldername != "ImageDataLocal":
                    #print(filename)
                    preencryptdata = b''
                    #readfile = file.read()
                    #preencryptdata += readfile
                    breadfile = file.read()
                    file.seek(-1, os.SEEK_END)
                    bytetest = file.read()
                    if bytetest == b'\x00':
                        readfile = breadfile[:-1]
                        removebytes = 1
                        dotruebytes = 1
                    elif bytetest == b'\x01':
                        readfile = breadfile[:-1]
                        removebytes = 1
                        dotruebytes = 1
                    elif bytetest == b'\x02':
                        readfile = breadfile[:-2]
                        removebytes = 2
                        dotruebytes = 1
                    elif bytetest == b'\x03':
                        readfile = breadfile[:-3]
                        removebytes = 3
                        dotruebytes = 1
                    elif bytetest == b'\x04':
                        readfile = breadfile[:-4]
                        removebytes = 4
                        dotruebytes = 1
                    elif bytetest == b'\x05':
                        readfile = breadfile[:-5]
                        removebytes = 5
                        dotruebytes = 1
                    elif bytetest == b'\x06':
                        readfile = breadfile[:-6]
                        removebytes = 6
                        dotruebytes = 1
                    elif bytetest == b'\x07':
                        readfile = breadfile[:-7]
                        removebytes = 7
                        dotruebytes = 1
                    elif bytetest == b'\x08':
                        readfile = breadfile[:-8]
                        removebytes = 8
                        dotruebytes = 1
                    elif bytetest == b'\t':
                        readfile = breadfile[:-9]
                        removebytes = 9
                        dotruebytes = 1
                    elif bytetest == b'\n':
                        superbytetest = file.seek(-2, os.SEEK_END)
                        duperbytetest = file.read()
                        if duperbytetest == b'\n\n':
                            readfile = breadfile[:-10]
                            removebytes = 10
                            dotruebytes = 1
                        else:
                            readfile = breadfile
                            removebytes = 0
                    elif bytetest == b'\x0b':
                        readfile = breadfile[:-11]
                        removebytes = 11
                        dotruebytes = 1
                    elif bytetest == b'\x0c':
                        readfile = breadfile[:-12]
                        removebytes = 12
                        dotruebytes = 1
                    elif bytetest == b'\r':
                        readfile = breadfile[:-13]
                        removebytes = 13
                        dotruebytes = 1
                    elif bytetest == b'\x0e':
                        readfile = breadfile[:-14]
                        removebytes = 14
                        dotruebytes = 1
                    elif bytetest == b'\x0f':
                        readfile = breadfile[:-15]
                        removebytes = 15
                        dotruebytes = 1
                    elif bytetest == b'\x10':
                        readfile = breadfile[:-16]
                        removebytes = 16
                        dotruebytes = 1
                    else:
                        readfile = breadfile
                        removebytes = 0
                    filesizerinos = sys.getsizeof(readfile)-17
                    filesizery = filesizerinos%16
                    
                    #rawpackfile.write(readfile)
                    preencryptdata += readfile
                    
                    if filesizery == 0:
                        ptruebytes = 16
                    else:
                        ptruebytes = 16-filesizery
                    # Now we start writing
                    if ptruebytes == 1:
                        preencryptdata += b'\x01'
                    elif ptruebytes == 2:
                        preencryptdata += b'\x02'
                        preencryptdata += b'\x02'
                    elif ptruebytes == 3:
                        preencryptdata += b'\x03'
                        preencryptdata += b'\x03'
                        preencryptdata += b'\x03'
                    elif ptruebytes == 4:
                        preencryptdata += b'\x04'
                        preencryptdata += b'\x04'
                        preencryptdata += b'\x04'
                        preencryptdata += b'\x04'
                    elif ptruebytes == 5:
                        preencryptdata += b'\x05'
                        preencryptdata += b'\x05'
                        preencryptdata += b'\x05'
                        preencryptdata += b'\x05'
                        preencryptdata += b'\x05'
                    elif ptruebytes == 6:
                        preencryptdata += b'\x06'
                        preencryptdata += b'\x06'
                        preencryptdata += b'\x06'
                        preencryptdata += b'\x06'
                        preencryptdata += b'\x06'
                        preencryptdata += b'\x06'
                    elif ptruebytes == 7:
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                        preencryptdata += b'\x07'
                    elif ptruebytes == 8:
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                        preencryptdata += b'\x08'
                    elif ptruebytes == 9:
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                        preencryptdata += b'\x09'
                    elif ptruebytes == 10:
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                        preencryptdata += b'\x0a'
                    elif ptruebytes == 11:
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                        preencryptdata += b'\x0b'
                    elif ptruebytes == 12:
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                        preencryptdata += b'\x0c'
                    elif ptruebytes == 13:
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                        preencryptdata += b'\x0d'
                    elif ptruebytes == 14:
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                        preencryptdata += b'\x0e'
                    elif ptruebytes == 15:
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                        preencryptdata += b'\x0f'
                    elif ptruebytes == 16:
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                        preencryptdata += b'\x10'
                    encrypteddata = encrypt(preencryptdata)
                    rawpackfile.write(encrypteddata)
                else:
                    readfile = file.read()
                    rawpackfile.write(readfile)
                filesize = os.path.getsize("%s/%s" % (path, filename))
                listfile.write("%s,%s,%s" % (filename, str(fileoffset), str(filesize+ptruebytes-removebytes)))
                listfile.write(chr(0x0a))
                fileoffset += filesize
                if dotruebytes == 1:
                    fileoffset += ptruebytes
                    fileoffset -= removebytes
                    dotruebytes = 0
                else:
                    fileoffset += ptruebytes
        rawpackfile.close()
        my_path = os.path.dirname(__file__)
        listfile.close()
        listfilepath = os.path.join(my_path, "temp.list")
        listfilesize = os.path.getsize(listfilepath)
        newlistfile = open("temp.list","ab")
        bytestoaddtolistfile = listfilesize%16
        if bytestoaddtolistfile == 0:
            truebytes = 16
        else:
            truebytes = 16-bytestoaddtolistfile
        if truebytes == 1:
            newlistfile.write(b'\x01')
        elif truebytes == 2:
            newlistfile.write(b'\x02')
            newlistfile.write(b'\x02')
        elif truebytes == 3:
            newlistfile.write(b'\x03')
            newlistfile.write(b'\x03')
            newlistfile.write(b'\x03')
        elif truebytes == 4:
            newlistfile.write(b'\x04')
            newlistfile.write(b'\x04')
            newlistfile.write(b'\x04')
            newlistfile.write(b'\x04')
        elif truebytes == 5:
            newlistfile.write(b'\x05')
            newlistfile.write(b'\x05')
            newlistfile.write(b'\x05')
            newlistfile.write(b'\x05')
            newlistfile.write(b'\x05')
        elif truebytes == 6:
            newlistfile.write(b'\x06')
            newlistfile.write(b'\x06')
            newlistfile.write(b'\x06')
            newlistfile.write(b'\x06')
            newlistfile.write(b'\x06')
            newlistfile.write(b'\x06')
        elif truebytes == 7:
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
            newlistfile.write(b'\x07')
        elif truebytes == 8:
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
            newlistfile.write(b'\x08')
        elif truebytes == 9:
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
            newlistfile.write(b'\x09')
        elif truebytes == 10:
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
            newlistfile.write(b'\x0a')
        elif truebytes == 11:
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
            newlistfile.write(b'\x0b')
        elif truebytes == 12:
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
            newlistfile.write(b'\x0c')
        elif truebytes == 13:
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
            newlistfile.write(b'\x0d')
        elif truebytes == 14:
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
            newlistfile.write(b'\x0e')
        elif truebytes == 15:
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
            newlistfile.write(b'\x0f')
        elif truebytes == 16:
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
            newlistfile.write(b'\x10')
        newlistfile.close()
        newerlistfile = open("temp.list","rb")
        newestlistfile = open("%s.list" % (foldername),"wb")
        list_file_data = newerlistfile.read()
        listfileencrypted = encrypt2("pack", list_file_data)
        newestlistfile.write(listfileencrypted)
        newestlistfile.close()
        rerawpackfile = open("temp.pack","rb")
        ready = rerawpackfile.read() 
        '''
        file_list = list_file_data.decode().split("\n")
        num_files = int(file_list[0])
        file_list = file_list[1:]
        '''
        packfile = open("%s.pack" % (foldername),"wb")
        '''
        if foldername != "ImageDataLocal":
            try:
                   for i in range(0, num_files):
                        file_info = file_list[i].split(",")
                        file_name = file_info[0]
                        file_offset = int(file_info[1])
                        file_size = int(file_info[2])
                        file_data = ready[file_offset:file_offset+file_size]
                        readiest = encrypt(file_data)
                        packfile.write(readiest)
            except:
                    print ("Tis I, error.") 
                    rerawpackfile.close()
                    os.remove("temp.pack")
                    os.remove("%s.list" % (foldername))
        '''
        packfile.write(ready)
        '''
        else:
            readiest = ready
            packfile = open("%s.pack" % (foldername),"wb")
            packfile.write(readiest)
            rerawpackfile.close()
            packfile.close()
        '''
        newerlistfile.close()
        rerawpackfile.close()
        packfile.close()
        os.remove("temp.list")
        os.remove("temp.pack")