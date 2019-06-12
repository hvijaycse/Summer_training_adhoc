#!/usr/bin/python36

data=input("Please enter data \n")[:499].split()
words={}
chars={}
for word in data:
    if word in words:
        words[word]+=1
    else :
        words[word]=1
    for c in word:
        if c in chars:
            chars[c]+=1
        else:
            chars[c]=1

list_word=[]
list_char=[]
for w,n in words.items():
    list_word.append((n,w))
for c,n in chars.items():
    list_char.append((n,c))
list_word.sort()
list_char.sort()
list_char.reverse()
list_word.reverse()
print(type(list_char[0]))
print(list_word)
print(" \n\n")
print(list_char)
#print("Repeated Characters in decending order \n"+' \\ '.join(list_char))
#print("\n\nRepeated words in decending order \n"+' \\ '.join(list_word))
