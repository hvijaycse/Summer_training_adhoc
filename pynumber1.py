import numpy as np
import random

list=[]
shape=input("Please Enter shape of array in aXb format").split('X')
for  i in range(int(shape[0])):
  temp_list=[]
  for t in range(int(shape[1])):
    temp_list.append(random.randrange(1,200))
  list.append(temp_list)

array=np.array(list)

print(array) # displaying array

store=open('array.txt','w')
store.write(str(array))
store.close()
