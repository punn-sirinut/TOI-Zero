n,m=map(int,input().split())
bomb_count=int(input())
grid=[[0 for i in range(m)] for i in range(n)]
bombs=[]
for i in range(bomb_count):
    r,c=map(int,input().split())
    bombs.append((r,c))
    grid[r][c]='x'
directions=[(-1, -1),(-1, 0),(-1, 1),
            (0, -1),         (0, 1),
            (1, -1),(1, 0),(1, 1)]
for r,c in bombs:
    for dr,dc in directions:
        nr,nc=r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            if grid[nr][nc]!='x':
                grid[nr][nc]+=1
for row in grid:
    print(" ".join(str(cell) for cell in row))