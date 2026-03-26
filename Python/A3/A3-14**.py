n = int(input())
a = 0
b = 0
for _ in range(n):
    x = int(input())
    if x > 18:
        a += 1
    else:
        b += 1
print(max(0, a - b - 1) + n)