l,y,s=input().split(" ")
y=int(y)
s=int(s)
bonus=0
if l=="M":
    bonus+=1500
    if y<5:
        bonus+=(0.06*s)
    elif y>=5 and y<10:
        bonus+=(0.08*s)
    elif y>=10:
        bonus+=(0.10*s)
elif l=="B":
    bonus+=1000
    if y<5:
        bonus+=(0.05*s)
    elif y>=5 and y<10:
        bonus+=(0.06*s)
    elif y>=10:
        bonus+=(0.07*s)
elif l=="G":
    bonus+=500
    if y<5:
        bonus+=(0.04*s)
    elif y>=5 and y<10:
        bonus+=(0.05*s)
    elif y>=10:
        bonus+=(0.06*s)
else:
    bonus+=0
print(int(bonus))