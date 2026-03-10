from collections import Counter
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cnt = Counter()
distinct = 0
sets = 0
for i in range(n):
    x = int(input())
    if cnt[x] == 0:
        distinct += 1
    cnt[x] += 1
    while distinct == k:
        sets += 1
        for j in range(1, k + 1):
            cnt[j] -= 1
            if cnt[j] == 0:
                distinct -= 1
print(n - sets * k)