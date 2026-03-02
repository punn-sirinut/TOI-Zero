f,t=str(input()).split()
w=int(input())
if(f=="BKK" and t=="CNX"):
    print(10+w*30)
elif(f=="CNX" and t=="UBP"):
    print(15+w*40)
elif(f=="UBP" and t=="BKK"):
    print(20+w*40)
elif(f=="BKK" and t=="PKT"):
    print(25+w*50)
elif(f=="PKT" and t=="CNX"):
    print(30+w*60)
elif(f=="UBP" and t=="PKT"):
    print(40+w*70)
else:
    print("Error")