n=int(input())
for i in range(n):
    x,y,z=map(float,input().split())
    sum=x+y+z
    op=[]
    if sum>=50:op.append("Overloaded")
    if x>=20:op.append("Check Type Plastic")
    if y>=20:op.append("Check Type Can")
    if z>=20:op.append("Check Type Glass")
    print(f"{sum:.1f}"+(","+",".join(op) if op else ""))