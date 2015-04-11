import sys
sys.setrecursionlimit(1024*1024)
INF = 1000000000

def dfs(l, s, L, n):
  print(len(l))
  if len(l) == L:
    if sorted(l) == sorted(s):
      return n
    else:
      return INF
  return min(dfs(l[:] + ['0'], s, L, n + 1),
      dfs(l[:] + ['1'], s, L, n + 1))

T = int(input())
for t in range(T):
  N, L = map(int, input().split())
  l = input().split()
  s = input().split()
  a = dfs(l, s, L, 0)
  print("Case #%d: " % (t + 1) + "NOT POSSIBLE" if a == INF else a) 
