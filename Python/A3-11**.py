n = int(input())
a = list(map(int, input().split()))
prefix = [0]
for x in a:
    prefix.append(prefix[-1] + x)
sums = set()
for i in range(n):
    for j in range(i+1, n+1):
        sums.add(prefix[j] - prefix[i])
print(len(sums))