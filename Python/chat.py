#!/usr/bin/python2
import threading
import socket
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
choose=input("Sender(s) or Reciver(r)")
def reciving(s,name):
	while True:
		new=s.recvfrom(125)[0].decode('ascii')
		if "$$$" in new:
			print("exiting")
			exit()
		print("\n"+name+new)
print("Enter $$$ to exit the chat")
if choose.lower()=='s':
	ip=input("Enter Reciver ip ")
	s.sendto("connecting".encode('ascii'),(ip,port))
	print(s.recvfrom(125)[0].decode('ascii'))
	rec=threading.Thread(target=reciving,args=(s,"Reciver: ",))
	rec.start()
	while True:
		send=input("Enter message: ")
		s.sendto(send.encode('ascii'),(ip,port))
		if "$$$" in send:
			print("exiting")
			s.close()
			exit()


if choose.lower()=='r':
	ip=socket.gethostbyname(socket.gethostname())
	print("My IP is : "+ip)
	s.bind((ip,port))
	soc=s.recvfrom(125)[1]
	s.sendto("connected to reciver".encode('ascii'),soc)
	print("Connected to Sender")
	rec=threading.Thread(target=reciving,args=(s,"Sender: ",))
	rec.start()
	while True:
		send=input("Enter message: ")
		s.sendto(send.encode('ascii'),soc)
		if "$$$" in send:
			print("exiting")
			s.close()
			exit()
s.close()
