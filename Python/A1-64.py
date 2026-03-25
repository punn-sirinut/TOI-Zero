s=input().split(" ")
n=int(s[0])
s=s[1:]
score=0
for i in range(n):
    if s[i]=="+":
        score+=10
    elif s[i]=="-":
        score-=5
print(score)