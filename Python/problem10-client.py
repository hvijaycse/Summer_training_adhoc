#!/usr/bin/python2
import socket
import time
#this_is_reciver(Client)                                                                                
port=10000
ip=raw_input("Enter server ip")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending message to send reciver ip
s.sendto("Hi there",(ip,port))
option=raw_input("Enter option  1/2  ")
if option=='1':
	what=raw_input("Press S to send and R to recive")
	if what=='S':
		message=raw_input("Enter message : ")
		s.sendto(message,(ip,port)) 
	else:
		reci=s.recvfrom(1000)
		print("Reciver: "+reci[0])
elif option=='2':
	length=s.recvfrom(100)
	length=int(length[0])
 	#recived file length
	data=s.recvfrom(length)
	new=open('recived.txt','w')
	new.write(data[0])
s.close()
exit()  
