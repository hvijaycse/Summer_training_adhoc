#!/usr/bin/python36
import socket
import time 
#this_is_sender(server)

port=9999
ip=socket.gethostbyname(socket.gethostname())
print("Serve ip is : "+ip)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((ip,port))
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	print("Looking for reciver{client}")
	try:
		ipfind=str.decode(s.recvfrom(100))
		reciverip=ipfind[1]
		break
	except:
		print("No reciver found")
		time.sleep(1)

option=input("\nPress 1 for messaging\nPress 2 for file transfer\n")
if option=='1':
	what=input("Press S to send and R to recive")
	if what is S:
		message=input()
		s.sendto(str.encode(message),(reciver))
	else:
		reci=str.decode(s.recvfrom(1000))
		print("Reciver: "+reci[0])
elif option=='2':
	f=open(input("Enter file address : "),'r')
	data=f.read()
	#sending length
	s.sendto(str.encode((str(len(data)))),(reciver))
	time.sleep(2)
	#sending file data
	s.sendto(str.encode(data),(reciver))

exit()
