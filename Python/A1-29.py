text=input()
vovels=['a','e','i','o','u']
cnt=0
for i in range (len(text)):
    if text[i] in vovels:
        cnt+=1
print(cnt)