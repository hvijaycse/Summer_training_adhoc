#!/usr/bin/python2
import socket 
ip='127.0.0.1'
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
choice=raw_input("Choose sender(s) or reciver(r)")
print("Send $$$ for exiting chat")
if choice=='s':
	while True:
		while True:
			mes=raw_input("Enter message : ")
			if len(mes)>150:
				print("Error")
				continue
			else :
				break
		s.sendto(mes,(ip,port))
		if mes=="$$$":
			print("Exiting")
			s.close()
			exit()
		mes=s.recvfrom(150)
		if "$$$" in mes:
			print("exiting")
			s.close()
			exit()
		else:
			print("Message : "+mes[0])

else :
	s.bind((ip,port))
	while True:
		mes=s.recvfrom(150)
		if "$$$" in mes:
			print("exiting")
			s.close()
			exit()
		else:
			print("Message : "+mes[0])
		soc=mes[1]
		while True:
			mes=raw_input("Enter message : ")
			if len(mes)>150:
				print("Error")
				continue
			else :
				break
		s.sendto(mes,soc)
		if mes=="$$$":
			print("Exiting")
			s.close()
			exit()
s.close()


