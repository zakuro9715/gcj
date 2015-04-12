from math import ceil
T = int(input())
for t in range(T):
    N = int(input())
    x = list(sorted(map(int, input().split())))
    a = x[-1]
    for i in range(2, x[-1]):
        aa = 0
        for j in x:
            aa += max(0, ceil(j / i) - 1)
        a = min(a, i + aa)
    print('Case #{0}: {1}'.format(t + 1, a))
