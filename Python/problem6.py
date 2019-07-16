#!/usr/bin/python36
data=input("Enter file name and operation seperated by :\n Enter file name only for normal operation\t")
data=data.split(':')
if len(data)<2:
	operation='no'
	name=data[0]
else :
	operation=data[1]
	name=data[0]
	
try:
	f=open(name,'r')
except:
	print(name+": File does not exist")
	exit(277)
print("\n\n")

if operation=='no':
	print(f.read())
elif operation=='E':
	for line in f:
		print(line.strip()+"$")
elif operation=='n':
	count=1
	for line in f:
		print(str(count)+line.strip())
		count+=1
elif operation=='b':
	count=1
	for line in f:
		if len(line)<1:
			print()
		else:
			print(str(count)+line.strip())
			count+=1			 

