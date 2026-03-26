m=int(input())
d=int(input())
if d>=21:
    if m==12 or m==1 or m==2:
        print("winter")
    elif m==3 or m==4 or m==5:
        print("spring")
    elif m==6 or m==7 or m==8:
        print("summer")
    elif m==9 or m==10 or m==11:
        print("fall")
else:
    if m==1 or m==2 or m==3:
        print("winter")
    elif m==4 or m==5 or m==6:
        print("spring")
    elif m==7 or m==8 or m==9:
        print("summer")
    elif m==10 or m==11 or m==12:
        print("fall")