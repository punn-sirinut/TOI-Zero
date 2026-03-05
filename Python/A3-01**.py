import sys
sys.setrecursionlimit(10**7)
adj = [[] for i in range(1005)]
def dfs(u):
    values = []
    for t, v in adj[u]:
        values.append(v if t == 1 else dfs(v)[0])
    left, right = values
    cost = abs(left - right)
    return 2 * max(left, right), cost
def solve():
    n = int(input())
    for i in range(1, n + 1):
        a, l, b, r = map(int, input().split())
        adj[i] = [(a, l), (b, r)]
    _, total_cost = accumulate_dfs(1)
    print(total_cost)
def accumulate_dfs(u):
    values = []
    total = 0
    for t, v in adj[u]:
        if t == 1:
            values.append(v)
        else:
            val, cost = accumulate_dfs(v)
            values.append(val)
            total += cost
    left, right = values
    total += abs(left - right)
    return 2 * max(left, right), total
solve()