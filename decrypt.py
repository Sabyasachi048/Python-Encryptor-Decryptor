# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:07:30 2019

@author: Sabyasachi
"""
def decrypt(filename,d,n):
    f3 = open(filename, 'r')
    str2=f3.read()
    en=[]
    de=[]
    en2 = str2.split(" ")
    for x in en2:
        if len(x) > 0:
            en.append(int(x))
    for x in en:
        de.append(pow(x, d,n))
    bytearray(de[:4])
    f2 = open(filename[:-4], 'wb')
    f2.write(bytearray(de))
    f2.close()
    print("decrypt msg: ", de)
    print("decryption complete")