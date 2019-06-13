#!/usr/bin/python2
import socket
import time 
#this_is_sender(server)

port=10000
ip=socket.gethostbyname(socket.gethostname())
print("Serve ip is : "+ip)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))
print("Looking for reciver")
ipfind=s.recvfrom(100)
resoc=ipfind[1]
print("Reciver Found")
option=raw_input("\nPress 1 for messaging\nPress 2 for file transfer\n")
if option=='1':
	what=raw_input("Press S to send and R to recive")
	if what=='S':
		message=raw_input()
		s.sendto(message,resoc)
	else:
		reci=s.recvfrom(1000)
		print("Reciver: ",reci[0])
elif option=='2':
	f=open(raw_input("Enter file address : "),'r')
	data=f.read()
	#sending length
	length=str(len(data))
	s.sendto(length,resoc)
	time.sleep(2)
	#sending file data
	s.sendto(data,resoc)
s.close()

exit()
