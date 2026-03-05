n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = y = 1
cnt = 0
for xx, yy in zip(a, b):
    p, pp = sorted((x, xx))
    q, qq = sorted((y, yy))
    same_segment = (p, pp) == (q, qq)
    disjoint_endpoints = (
        p not in (q, qq) and
        pp not in (q, qq)
    )
    cross_1 = p < q < pp < qq
    cross_2 = q < p < qq < pp
    if same_segment or (disjoint_endpoints and (cross_1 or cross_2)):
        cnt += 1
    x, y = xx, yy
print(cnt)