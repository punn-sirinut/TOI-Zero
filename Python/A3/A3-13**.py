n, s = map(int, input().split())
mn = mx = 0
for i in range(n):
    k = int(input())
    a = k//3*10
    b = k//4*10
    if k%3==0 and k%4!=0:
        mn+=a; mx+=a
    elif k%4==0 and k%3!=0:
        mn+=b; mx+=b
    else:
        mn+=min(a,b); mx+=max(a,b)
print(s-mx, s-mn)