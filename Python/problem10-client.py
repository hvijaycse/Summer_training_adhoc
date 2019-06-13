#!/usr/bin/python36
import socket
import time
#this_is_reciver(Client)                                                                                
port=9999
ip=input("Enter server ip")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to send reciver ip
s.sendto(str.encode("Hi there"),ip)
option=input("Enter option")
if option=='1':
	what=input("Press S to send and R to recive")
	if what=='S':
		message=input()
		s.sendto(str.encode(message),(reciver)) 
	else:
		reci=str.decode(s.recvfrom(1000))
		print("Reciver: "+reci[0])
elif option=='2':
	length=s.recvfrom(100)
	length=int(length[0])
 	#recived file length
	data=s.recvfrom(length)
	new=open('recived.txt','w')
	new.write(data[0])
exit()  
