#!/usr/bin/python36
import os

num=[]
for i in range(0,9):
	num.append(str(i))
username=input("Enter username you want to add \t")
for i in username:
	if i in num:
		exit("Username can't have integer in them")

os.system('sudo useradd -p '+username+'{hello} '+username) 
print("operation successfull")

