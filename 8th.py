import sys


def pos(t, p, k):
    s = p + t
    n = len(s)
    z = [[0] * (k + 1) for i in range(n)]
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i][0] = min(z[i - l][0], r - i + 1)
        while i + z[i][0] < n and s[i + z[i][0]] == s[z[i][0]]:
            z[i][0] += 1
        if i + z[i][0] > r:
            l, r = i, i + z[i][0] - 1
        for j in range(1, k + 1):
            z[i][j] = min(z[i][j - 1] + 1, n - i)
            while i + z[i][j] < n and s[i + z[i][j]] == s[z[i][j]]:
                z[i][j] += 1
        if z[i][k] >= len(p) and i >= len(p):
            yield i - len(p)


sys.stdin = open('input.txt', "r")
for line in sys.stdin:
    k, t, p = line.split()
    k = int(k)
    ans = list(pos(t, p, k))
    print(len(ans), *ans)