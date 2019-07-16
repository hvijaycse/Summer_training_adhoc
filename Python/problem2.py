#!/usr/bin/python36

#you need to install google library for this program
#install via 'pip install google'

import webbrowser
from googlesearch import search
fil=open('url.txt','a+')
data=input("Enter data to be searched \t")
searched=search(data,stop=10)
for url in searched:
	fil.write(url+"\n\n")
	webbrowser.open(url)

	

