n=int(input())
s=list(map(int,input().split()))
sum=0
cnt=0
for i in range(n):
    sum+=s[i]
avg=sum/n
print(f"{avg:.1f}")
if avg>=60:
    for i in range(n):
        if s[i]>=50:
            cnt+=1
    if cnt==n:
        print("PASS")
    else:
        print("FAIL")
else:
    print("FAIL")