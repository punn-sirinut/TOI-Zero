CHE=0
LIV=0
MUN=0
NEW=0
m,n=map(int,input().split())
if m>n:
    CHE+=3
elif m<n:
    LIV+=3
elif m==n:
    CHE+=1
    LIV+=1
m,n=map(int,input().split())
if m>n:
    CHE+=3
elif m<n:
    MUN+=3
elif m==n:
    CHE+=1
    MUN+=1
m,n=map(int,input().split())
if m>n:
    CHE+=3
elif m<n:
    NEW+=3
elif m==n:
    CHE+=1
    NEW+=1
m,n=map(int,input().split())
if m>n:
    LIV+=3
elif m<n:
    MUN+=3
elif m==n:
    LIV+=1
    MUN+=1
m,n=map(int,input().split())
if m>n:
    LIV+=3
elif m<n:
    NEW+=3
elif m==n:
    LIV+=1
    NEW+=1
m,n=map(int,input().split())
if m>n:
    MUN+=3
elif m<n:
    NEW+=3
elif m==n:
    MUN+=1
    NEW+=1
if CHE>=LIV and CHE>=MUN and CHE>=NEW:
    print(f"1. CHE {CHE}")
    if LIV>=MUN and LIV>=NEW:
        print(f"2. LIV {LIV}")
        if MUN>=NEW:
            print(f"3. MUN {MUN}")
            print(f"4. NEW {NEW}")
        elif NEW>MUN:
            print(f"3. NEW {NEW}")
            print(f"4. MUN {MUN}")
    elif MUN>=LIV and MUN>=NEW:
        print(f"2. MUN {MUN}")
        if LIV>=NEW:
            print(f"3. LIV {LIV}")
            print(f"4. NEW {NEW}")
        elif NEW>=LIV:
            print(f"3. NEW {NEW}")
            print(f"4. LIV {LIV}")
    elif NEW>=LIV and NEW>=MUN:
        print(f"2. NEW {NEW}")
        if LIV>=MUN:
            print(f"3. LIV {LIV}")
            print(f"4. MUN {MUN}")
        elif MUN>=LIV:
            print(f"3. MUN {MUN}")
            print(f"4. LIV {LIV}")
elif LIV>=CHE and LIV>=MUN and LIV>=NEW:
    print(f"1. LIV {LIV}")
    if CHE>=MUN and CHE>=NEW:
        print(f"2. CHE {CHE}")
        if MUN>=NEW:
            print(f"3. MUN {MUN}")
            print(f"4. NEW {NEW}")
        elif NEW>=MUN:
            print(f"3. NEW {NEW}")
            print(f"4. MUN {MUN}")
    elif MUN>=CHE and MUN>=NEW:
        print(f"2. MUN {MUN}")
        if CHE>=NEW:
            print(f"3. CHE {CHE}")
            print(f"4. NEW {NEW}")
        elif NEW>=CHE:
            print(f"3. NEW {NEW}")
            print(f"4. CHE {CHE}")
    elif NEW>=CHE and NEW>=MUN:
        print(f"2. NEW {NEW}")
        if CHE>=MUN:
            print(f"3. CHE {CHE}")
            print(f"4. MUN {MUN}")
        elif MUN>=CHE:
            print(f"3. MUN {MUN}")
            print(f"4. CHE {CHE}")
elif MUN>=CHE and MUN>=LIV and MUN>=NEW:
    print(f"1. MUN {MUN}")
    if CHE>=LIV and CHE>=NEW:
        print(f"2. CHE {CHE}")
        if LIV>=NEW:
            print(f"3. LIV {LIV}")
            print(f"4. NEW {NEW}")
        elif NEW>=LIV:
            print(f"3. NEW {NEW}")
            print(f"4. LIV {LIV}")
    elif LIV>=CHE and LIV>=NEW:
        print(f"2. LIV {LIV}")
        if CHE>=NEW:
            print(f"3. CHE {CHE}")
            print(f"4. NEW {NEW}")
        elif NEW>=CHE:
            print(f"3. NEW {NEW}")
            print(f"4. CHE {CHE}")
    elif NEW>=CHE and NEW>=LIV:
        print(f"2. NEW {NEW}")
        if CHE>=LIV:
            print(f"3. CHE {CHE}")
            print(f"4. LIV {LIV}")
        elif LIV>=CHE:
            print(f"3. LIV {LIV}")
            print(f"4. CHE {CHE}")
elif NEW>=CHE and NEW>=LIV and NEW>=MUN:
    print(f"1. NEW {NEW}")
    if CHE>=LIV and CHE>=MUN:
        print(f"2. CHE {CHE}")
        if LIV>=MUN:
            print(f"3. LIV {LIV}")
            print(f"4. MUN {MUN}")
        elif MUN>=LIV:
            print(f"3. MUN {MUN}")
            print(f"4. LIV {LIV}")
    elif LIV>=CHE and LIV>=MUN:
        print(f"2. LIV {LIV}")
        if CHE>=MUN:
            print(f"3. CHE {CHE}")
            print(f"4. MUN {MUN}")
        elif MUN>=CHE:
            print(f"3. MUN {MUN}")
            print(f"4. CHE {CHE}")
    elif MUN>=CHE and MUN>=LIV:
        print(f"2. MUN {MUN}")
        if CHE>=LIV:
            print(f"3. CHE {CHE}")
            print(f"4. LIV {LIV}")
        elif LIV>=CHE:
            print(f"3. LIV {LIV}")
            print(f"4. CHE {CHE}")