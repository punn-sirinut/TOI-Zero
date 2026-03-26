n = int(input())
points = [(x + y, x - y)
          for x, y in (map(int, input().split()) for i in range(n))]
xs = sorted(p[0] for p in points)
ys = sorted(p[1] for p in points)
sx = xs[n // 2]
sy = ys[n // 2]
ans = sum(abs(x - sx) + abs(y - sy) for x, y in points)
print(ans)