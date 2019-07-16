#!/usr/bin/python36
import pyttsx3
import time 
engine=pyttsx3.init()
hour=int(time.asctime().split[3.split(':')[0]])
name=input("Enter you name")
engine.say("HI there "+name)
if hour<12:
	engine.say("Good morning")
elif hour<15:
	engine.say("Good evening")
elif hour<16:
	engine.say("Good afternoon")
else :	
	engine.say("Good night")
def adder(*s)
	sum=0
	for i in s:
		sum+=i
	return sum
def sorter(*s):
	return s.sort()
def module():
	print("Printing installed Moduels"
	help('modules')
