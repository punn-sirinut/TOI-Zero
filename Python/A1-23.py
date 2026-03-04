temp=int(input())
s=input().upper()
if s=="C":
    if temp <= 0:
        print("solid")
    elif temp>=100:
        print("gas")
    else:
        print("liquid")
elif s=="F":
    if temp <= 32:
        print("solid")
    elif temp>=212:
        print("gas")
    else:
        print("liquid")