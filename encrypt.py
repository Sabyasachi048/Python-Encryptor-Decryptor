# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:00:27 2019

@author: Sabyasachi
"""
def encrypt(filename,e,n):
    with open(filename, "rb") as image:
        f = image.read()
        msg = bytearray(f)
    en = []
    print("msg: ", msg)
    for x in msg:
        en.append(pow(x, e, n))
    print("\nencrypt msg: ", en)
    ss = ""
    f3 = open(filename+'.enc', 'w')
    for x in en:
        ss += (str(x) + " ")
    f3.write(ss)
    print("Encryption complete")