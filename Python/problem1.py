#!/usr/bin/python36
import datetime
nm=input("Enter your name \t")
age=int(input('Enter you age \t'))
year=int(datetime.datetime.now().year)
year=year-age+95
print("HI "+nm+" you will turn 95 in year "+str(year))

