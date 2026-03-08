n=int(input())
temp=input().split(" ")
temp=[float(i) for i in temp]
temp.sort()
sum=0
alert=0
for i in range(n):
    sum+=temp[i]
    if(temp[i]>=37):alert+=1
avg=sum/n
if(n%2==0):
    med=(temp[n//2-1]+temp[n//2])/2
else:
    med=temp[n//2]
print(f"SUM={sum:.2f}")
print(f"AVG={avg:.2f}")
print(f"MEDIAN={med:.2f}")
print(f"MAX={temp[-1]:.2f}")
print(f"MIN={temp[0]:.2f}")
print(f"ALERT={alert}")
print(f"SORTED={' '.join([f'{i:.2f}' for i in temp])}")