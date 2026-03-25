x,y=map(int,input().split())
d=0
cnt=0
while x>0:
    cnt+=1
    d+=x
    x-=2
    if d>=y:
        print(cnt)
        break
else:
    print(-1)
    exit()