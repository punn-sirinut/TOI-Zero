r=list(map(int,input().split(" ")))
m=0
w=0
for i in range(len(r)):
    if r[i]%2==0:
        w+=1
    else:
        m+=1
if r[-1]%2==0:
    w-=1
else:
    m-=1
print(f"{m} {w} {m+w}")