#!/usr/bin/python36
import time

name=input("Please enter you name \t")
hour=int(time.asctime().split()[3].split(':')[0])
if hour<12:
	print("Good Morning "+name)
elif hour<15:
	print("Good Evening "+name)
elif hour<16:
	print("Good afternoon "+name)
else :	
	print("Good night "+name)


