from itertools import groupby
m, n = map(int, input().split())
events = []
for i in range(n):
    l, r = map(int, input().split())
    events.append((l, 1))
    events.append((r + 1, -1))
events.sort()
cnt = mx = 0
for i, group in groupby(events, key=lambda x: x[0]):
    cnt += sum(k for i, k in group)
    mx = max(mx, cnt)
print(mx)