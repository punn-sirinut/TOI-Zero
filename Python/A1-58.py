n=input()
n=int(n)
l=[]
all=0
for i in range(n):
    s=int(input())
    all+=s
    l.append(s)
l.sort()
print(all)
print(l[-1])
print(l[0])
print(f"{all/n:.1f}")