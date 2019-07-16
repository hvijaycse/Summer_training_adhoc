#!/usr/bin/python36

data=input("Please enter data \n")[:499]
print(len(data))
print()
print()
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
print("Words \n")
print(list_word)
print(" \n\nCharacters\n")
print(list_char)
#removing more than 5 words complete
for word in list_word:
    if word[0]>=5:
        while True:
            data.remove(word[1])
            if word[1] in data:
                continue
            else:
                break
        list_word.remove(word)
#adding word occuiirng once
for word in list_word:
    if word[0]==1:
        total_len=len(word[1])+len(data)
        if total_len<500:
            print(total_len)
            data.append(word[1])
        else:
            print("else executed")
            length=0
            while True:
                first=list_word[0]
                length+=len(first[1])
                if length <len(word[1]):
                    if first[0]==1:
                        list_word.remove(first)
                        data.remove(first[1])
                        continue
                    else:
                        data.remove(first[1])
                        list_word[0]=(first[0]-1,first[1])
                        continue
                else:
                    data.append(word[1])
        list_word[list_word.index(word)]=(word[0]+1,word[1])


print("\n\ndata after removing words occuring more than 5 times: \n\n")
print(' '.join(data))
print("\n\n")
print(list_word)
