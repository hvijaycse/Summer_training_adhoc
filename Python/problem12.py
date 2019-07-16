#!/usr/bin/python36
import qrcode
from googlesearch import search
html=open("/var/www/html/a.html",'a')
data=input("Enter Search\t")
urls=search(data,stop=3)
i=1
for url in urls:
	image=qrcode.make(url)
	with open("/var/www/html/"+data+str(i)+".png",'wb') as f:
		image.save(f)
	i+=1
	html.write('<h1>'+data+"</h1>")
	html.write("<img src="+'"'+data+str(i)+".png"+'">'+"\n")
print("qrcode made")
exit()	
