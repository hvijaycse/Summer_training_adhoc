import os

number=int(input("Input numbers of folder \n\t"))
name=input("Basic name of the folder\n\t")
if len(name)<1:
    name=" "

for i in range(number):
    command='rmdir '+name+str(i)
    os.system(command)
print("Directory  Deleted")
input()
