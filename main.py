# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:42:07 2019

@author: Sabyasachi
"""

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import math
import encrypt
import decrypt
import keygen
import hashlib
import base64


def encfile():
    filewin = Tk()
    filewin.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=[("all files", "*.*")])
    print(filewin.filename)
    if(len(filewin.filename) > 0):
        encrypt.encrypt(filewin.filename, e, n)
        os.remove(filewin.filename)
        messagebox.showinfo("Success!", "Encryption Complete")
    else:
        messagebox.showerror("Error!", "File does not exist")
    filewin.destroy()


def decfile():
    filewin = Tk()
    filewin.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("encrypted files", "*.enc"), ("all files", "*.*")))
    print(filewin.filename)
    if(len(filewin.filename) > 0):
        decrypt.decrypt(filewin.filename, d, n)
        os.remove(filewin.filename)
        messagebox.showinfo("Success!", "Decryption Complete")
    else:
        messagebox.showerror("Error!", "File does not exist")
    filewin.destroy()


def logout():
    softwin.destroy()
    main()


def soft():
    file = open(user+'.keys', 'r').readlines()
    global n, e, d
    n = file[0]
    e = file[1]
    d = file[2]
    # nE = base64.b64decode(n)
    # eE = base64.b64decode(e)
    # dE = base64.b64decode(d)
    n = int(n)
    e = int(e)
    d = int(d)
    print(n)
    print(e)
    print(d)
    window1.destroy()
    global softwin
    softwin = Tk()
    softwin.geometry("400x400")
    softwin.title("Encryption Decryption Software")
    userL = Label(softwin, text='Username:'+user)
    userL.place(relx=0.5, rely=0.2, anchor=CENTER)
    encryptbtn = Button(softwin, text='Encrypt', command=encfile)
# loginbtn.grid(row = 2,columnspan = 2,sticky=W)
    encryptbtn.place(relx=0.5, rely=0.5, anchor=CENTER)
    decryptbtn = Button(softwin, text='Decrypt', command=decfile)
# signupbtn.grid(columnspan = 2,sticky=W)
    decryptbtn.place(relx=0.5, rely=0.7, anchor=CENTER)
    logoutbtn = Button(softwin, text="Log out", command=logout)
    logoutbtn.place(relx=0.5, rely=0.9, anchor=CENTER)
    softwin.mainloop()


def signup():
    name = nameE.get()
    pword = passwordE.get()
    if len(name) > 0 and len(pword) > 0:
        filename = "./users/"+name+".creds"
        print(filename)
        exists = os.path.exists(filename)
        if exists:
            messagebox.showerror("Error!", "Username already exists")
        else:
            keygen.gen_key(name)
            file = open("./users/"+name+".creds", 'w+')
            hsh = name+pword
            hsh = hashlib.md5(hsh.encode())
            hsh = hsh.hexdigest()
            # file.write(name+'\n')
            # file.write(pword)
            file.write(hsh)
            file.close()
            messagebox.showinfo("Complete", "Signup has been complete")
            signwin.destroy()
    else:
        messagebox.showerror("Error!", "No Username or Password entered")


def fsignup():
    global signwin, nameE, passwordE
    signwin = Tk()
    signwin.title("Signup")
    signwin.geometry('300x300')
    nameL = Label(signwin, text='Username')
    passwordL = Label(signwin, text='Password')
    nameL.grid(row=1, column=0, sticky=W)
    passwordL.grid(row=2, column=0, sticky=W)
    nameE = Entry(signwin)
    passwordE = Entry(signwin, show='*')
    nameE.grid(row=1, column=1)
    passwordE.grid(row=2, column=1)
    signupbtn = Button(signwin, text='Sign up', command=signup)
    signupbtn.place(relx=0.5, rely=0.7, anchor=CENTER)
    signwin.mainloop()


def login():
    global user, pword
    user = userE.get()
    pword = passE.get()
    if len(user) > 0 and len(pword) > 0:
        exists = os.path.isfile("./users/"+user+'.creds')
        if exists:
            file = open("./users/"+user+'.creds', 'r')
            FLE = file.readlines()
#        x = file.read()
#        for i in file:
#            print(i)
            hsh = (user+pword)
            hsh = hashlib.md5(hsh.encode())
            hsh = hsh.hexdigest()
            x = FLE[0]
            # print("x: "+x, end=' ')
            # print("pword: "+pword)
            if(x == hsh):
                messagebox.showinfo("Successful", "Login Successful")
                loginwin.destroy()
                soft()
            else:
                messagebox.showerror(
                    "Wrong Password", "Wrong password entered")
            file.close()
        else:
            messagebox.showerror("Error!", "Username does not exist")
    else:
        messagebox.showerror('Error!', "No Username or Password entered")


def flogin():
    global loginwin, userE, passE
    loginwin = Tk()
    loginwin.title("Log in")
    loginwin.geometry('300x300')
    nameL = Label(loginwin, text='Username')
    passwordL = Label(loginwin, text='Password')
    nameL.grid(row=1, column=0, sticky=W)
    passwordL.grid(row=2, column=0, sticky=W)
    userE = Entry(loginwin)
    passE = Entry(loginwin, show='*')
    userE.grid(row=1, column=1)
    passE.grid(row=2, column=1)
    loginbtn = Button(loginwin, text='Login', command=login)
    loginbtn.place(relx=0.5, rely=0.7, anchor=CENTER)
    loginwin.mainloop()


def main():
	if not os.path.exists("./users/"):
		os.makedirs("./users/")
	global window1
	window1 = Tk()
	window1.geometry('300x200')
	window1.title('Encryption Decryption software')
	loginbtn = Button(window1, text='Login', command=flogin)
# loginbtn.grid(row = 2,columnspan = 2,sticky=W)
	loginbtn.place(relx=0.5, rely=0.5, anchor=CENTER)
	signupbtn = Button(window1, text='Sign up', command=fsignup)
# signupbtn.grid(columnspan = 2,sticky=W)
	signupbtn.place(relx=0.5, rely=0.7, anchor=CENTER)
	window1.mainloop()


main()
