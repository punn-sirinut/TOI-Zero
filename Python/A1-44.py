age,day=input().split()
age=int(age)
if age<5:
    p=0
elif age<19:
    p=100
else:
    p=150
if day=="Wed":p=p//2
print(p)