#!/usr/bin/python36
try:
	from selenium import webdriver
except:
	input(print("Please install selenium Library \nPrint enter to exit"))
	exit()
message='%'.join(input("Enter message to be sended\t"))
num=input("Please enter number of reciver with country code \t+")
url='https://web.whatsapp.com/send?phone='+num+'&text='+message+'&source=&data='
driver=webdriver.Chrome()
driver.get(url)

#this program is incomplete and will be made complete soon

