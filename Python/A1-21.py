y=int(input())
if y%400==0 or y==1500:
    print("yes")
elif y%100==0:
    print("no")
elif y%4==0:
    print("yes")
else:
    print("no")