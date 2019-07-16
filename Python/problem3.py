#!/usr/bin/python36
adhoc=[1,2,3,4,5,6,7,66,22,6,0,9]
five=[]
two=[]
for i in adhoc:
	if i>5:
		print("greater than 5 :"+str(i))
		five.append(i)
	if i<=2:
		print("Less than or equall to 2: "+str(i))
		two.append(i)

