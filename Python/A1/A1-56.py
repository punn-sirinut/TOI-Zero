x1,y1,z1=list(map(int,input().split()))
x2,y2,z2=list(map(int,input().split()))
d=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
d=f"{d:.2f}"
print(d)