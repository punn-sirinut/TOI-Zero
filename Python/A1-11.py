s=input()
r=[]
cnt=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt+=1
    else:
        r.append(f"{cnt}{s[i-1]}")
        cnt=1
r.append(f"{cnt}{s[-1]}")
print("".join(r))