# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:30:57 2019

@author: Sabyasachi
"""
import gmpy2
import random as rd
import math
import base64

def modinv(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0

    return x


def gen_key(file):
    x = pow(2,512)
    y = pow(2,513)-1
    p = rd.randrange(x,y)
    p = gmpy2.next_prime(p)
    q = gmpy2.next_prime(p)
    p=int(p)
    q=int(q)
    n = p*q
    phi = (p-1)*(q-1)
    e=2
    for i in range(3,phi,2):
        if math.gcd(i,phi)==1:
           e=i
           break
    d = modinv(e,phi)
    # n = str(n).encode('ascii')
    # e = str(e).encode('ascii')
    # d = str(d).encode('ascii')
    file = open(file+'.keys','w')
    file.write(str(n)+'\n')
#    file.write(str(phi)+'\n')
    file.write(str(e)+'\n')
    file.write(str(d)+'\n')
    file.close()    