l, n = map(int, input().split())
c = 0
while n > 0:
    c += 1
    for i in range(1, c * l + 1):
        n -= min(i, l)
        if(n <= 0):
            break
print(c)