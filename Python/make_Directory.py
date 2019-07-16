import os

number=int(input("\tInput numbers of folder \n\t"))
name=input("\tBasic name of the folder \n\t")
if len(name)<1:
    name=" "

for i in range(number):
    command='mkdir '+name+str(i)
    os.system(command)
print("Directory Created")
input()
