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
s.sendto(option,resoc)

def reciving(s,name):
	while True:
		new=s.recvfrom(125)[0].decode('ascii')
		if "$$$" in new:
			print("exiting")
			exit()
		print("\n"+name+new)

if option=='1':
	rec=threading.Thread(target=reciving,args=(s,"Reciver: ",))
	rec.start()
	while True:
		msg=raw_input("Enter your message")
		s.sednto(msg,(ip,port))
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
