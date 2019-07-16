#!/usr/bin/python2
import socket
import threading
#this_is_reciver(Client)                                                                                
port=10000
ip=raw_input("Enter server ip")
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending message to send reciver ip
s.sendto("connecting",(ip,port))
option=s.recvfrom()
soc=option[1]
option=option[0]
def reciving(s,name):
	while True:
		new=s.recvfrom(125)[0].decode('ascii')
		if "$$$" in new:
			print("exiting")
			exit()
		print("\n"+name+new)
if option=='1':
	rec=threading.Thread(target=reciving,args=(s,"Sender: ",))
	rec.start()
	while True:
		msg=raw_input("Enter your message")
		s.sednto(msg,(ip,port))
	
	
elif option=='2':
	length=s.recvfrom(100)
	length=int(length[0])
 	#recived file length
	data=s.recvfrom(length)
	new=open('recived.txt','w')
	new.write(data[0])
s.close()
exit()  
