n=int(input())
vovels=['A','E','I','O','U']
cnt=0
for i in range (n):
    s=input()
    if(s in vovels):cnt+=1
print(cnt)