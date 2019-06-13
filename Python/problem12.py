#!/usr/bin/python36
import qrcode
from googlesearch import search
data=input("Enter Search\t")
urls=search(data,stop=3)
i=1
for url in urls:
	image=qrcode.make(url)
	with open(data+str(i)+".png",'wb') as f:
		image.save(f)
	i+=1
print("qrcode made")
exit()	
