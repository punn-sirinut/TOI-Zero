n=int(input())
if str(n)[-1]!="0" or str(n)[-2]!="0" or n<100 or n>20000:
    print("ERROR")
    exit()
x=0
y=0
z=0
while n>0:
    if n>=1000:
        x+=1
        n-=1000
    elif n>=500:
        y+=1
        n-=500
    elif n>=100:
        z+=1
        n-=100
if x!=0:
    print(f"1000 = {x}")
if y!=0:
    print(f"500 = {y}")
if z!=0:
    print(f"100 = {z}")