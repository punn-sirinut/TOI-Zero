n=int(input())
num=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=num[i]
even=0
odd=0
for i in range(n):
    if num[i]%2==0:
        even+=1
    else:
        odd+=1
print(f"SUM {sum}")
print(f"EVEN {even}")
print(f"ODD {odd}")