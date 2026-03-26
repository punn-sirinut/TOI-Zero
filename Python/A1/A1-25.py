c=input()
c=c.upper()
if c[0]=='1':
    if c[-1]=="S":
        print(f"10 of spades")
    elif c[-1]=="H":
        print(f"10 of hearts")
    elif c[-1]=="D":
        print(f"10 of diamonds")
    elif c[-1]=="C":
        print(f"10 of clubs")
elif c[0]=="J":
    if c[-1]=="S":
        print(f"jack of spades")
    elif c[-1]=="H":
        print(f"jack of hearts")
    elif c[-1]=="D":
        print(f"jack of diamonds")
    elif c[-1]=="C":
        print(f"jack of clubs")
elif c[0]=="Q":
    if c[-1]=="S":
        print(f"queen of spades")
    elif c[-1]=="H":
        print(f"queen of hearts")
    elif c[-1]=="D":
        print(f"queen of diamonds")
    elif c[-1]=="C":
        print(f"queen of clubs")
elif c[0]=="K":
    if c[-1]=="S":
        print(f"king of spades")
    elif c[-1]=="H":
        print(f"king of hearts")
    elif c[-1]=="D":
        print(f"king of diamonds")
    elif c[-1]=="C":
        print(f"king of clubs")
elif c[0]=="A":
    if c[-1]=="S":
        print(f"ace of spades")
    elif c[-1]=="H":
        print(f"ace of hearts")
    elif c[-1]=="D":
        print(f"ace of diamonds")
    elif c[-1]=="C":
        print(f"ace of clubs")
else:
    if c[-1]=="S":
        print(f"{c[0]} of spades")
    elif c[-1]=="H":
        print(f"{c[0]} of hearts")
    elif c[-1]=="D":
        print(f"{c[0]} of diamonds")
    elif c[-1]=="C":
        print(f"{c[0]} of clubs")