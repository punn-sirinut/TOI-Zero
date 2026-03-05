n = int(input())
weights = [
    w
    for i in range(1, 201)
    for w in ([2 * i] * 9 + [i])
]
a = sorted(map(int, input().split()), reverse=True)
weights.sort()
ans = sum(x * w for x, w in zip(a, weights))
print(ans)