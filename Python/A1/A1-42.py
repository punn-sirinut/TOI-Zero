x=0
y=0
s=str(input())
for i in range(len(s)):
    if s[i]=="W":
        x-=1
    elif s[i]=="E":
        x+=1
    elif s[i]=="N":
        y+=1
    elif s[i]=="S":
        y-=1
d=abs(x)+abs(y)
print(x,y,d)