import random
import numpy as np

start=random.randrange(100,120)

list=[]
for i in range(2):
    last=start
    temp_list=[]
    for i in range(8):
        temp_list.append(last+5)
        last+=5
    start=last
    list.append(temp_list)
arr=np.array(list)

print(arr)
input("Enter to exit")
