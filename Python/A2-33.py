i=float(input())
o=float(input())
if(i<0 or o<0 or i>24 or o>24):
    print("ERROR")
    exit()
t=o-i
if(t<0.15):print("FREE")
elif(t<=1):print(25)
elif(t<=2):print(50)
elif(t<=3):print(80)
elif(t<=4):print(110)
elif(t<=5):print(145)
elif(t<=6):print(180)
else:print(250)