import os
import pyttsx3
previous=[]
engine=pyttsx3.init()
f=open("commands.txt",'w+')
def check(com):
        return os.system(com+" &>/dev/null &")
while True:
        command=input("\n \t Please enter command\t")
        if command=="exit":
                print("exiting")
                exit(0)
        if command in previous:
		engine.say("Error : Previous commad")
                print("Please do not enter old command")
                continue
        else:
                previous.append(command)
                f.write(command)
                if check(command)==0:
                        os.system(command)
                else:
                        print("Error Command not found")
