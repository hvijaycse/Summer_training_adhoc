import random,string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

s=[]
y=int(input("Enter numbers of variables"))
for i in range(y):
    s.append(randomword(random.choice(range(5))))
print(s)

print("Done")
input()
