from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot  as plt

url='https://en.wikipedia.org/wiki/Machine_learning'
webpage=requests.get(url)
soup=BeautifulSoup(webpage.text,features="lxml")

para=[]
word_count={}
words=[]

words=soup.get_text().split()

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
words=[]
for word,num in word_count.items():

    words.append((num,word))
words.sort()
words.reverse()

print("There are " +str(len(words))+" words in this webpage" )

#creating a numpy datatype for easy access
plot_data=pd.DataFrame(words)
words=list(plot_data.iloc[0:,1])
counts=list(plot_data.iloc[0:,0])
#accesing data for plotting

top20=counts[0:20]
top20_words=words[0:20]
#last3wordspostion
counts.reverse()
pos=len(counts)-counts.index(3)
counts.reverse()

words_above_3=words[:pos]
count_above_3=counts[:pos]
#plotting top20

plt.title("Top 20 words")
plt.pie(top20,labels=top20_words)
plt.show()
#top 20 bar
plt.title("Top 20 word")
plt.bar(top20_words,top20)
plt.xlabel("Words")
plt.ylabel("Occurance")
plt.xticks(rotation=90)
plt.show()
#all above 3 in scatter
plt.title("Words above count 3")
plt.scatter(words_above_3,count_above_3)
plt.xlabel("words")
plt.ylabel("Occurance")
plt.xticks(rotation=90)
plt.show()
