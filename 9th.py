import sys


def z_function(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i] - 1
    return z


def step(ln, k, prev):
    res = k + 2 + len(str(ln // k))
    if ln == k:
        res -= 2
    if prev == n:
        res -= 1
    return res


sys.stdin = open('input.txt', "r")
s = input()
n = len(s)
s += '_'
dp = [n - i for i in range(n + 1)]
to = [[n - i, n - i] for i in range(n + 1)]
for i in range(n - 2, -1, -1):
    z = z_function(s[i:])
    if dp[i] > dp[i + 1] + 2:
        dp[i] = dp[i + 1] + 2
        to[i] = [1, 1]
    for j in range(i + 1, n + 1):
        k = 1
        while k * k <= j - i:
            if (j - i) % k:
                k += 1
                continue
            if z[k] + k >= j - i:
                if dp[i] > dp[j] + step(j - i, k, j):
                    dp[i] = dp[j] + step(j - i, k, j)
                    to[i] = [j - i, k]
            if z[(j - i) // k] + (j - i) // k >= j - i:
                if dp[i] > dp[j] + step(j - i, (j - i) // k, j):
                    dp[i] = dp[j] + step(j - i, (j - i) // k, j)
                    to[i] = [j - i, (j - i) // k]
            k += 1

with open('output.txt', 'w') as f_out:
    i = 0
    while i < n:
        if i > 0:
            f_out.writelines('+')
        f_out.writelines(s[i: i + to[i][1]])
        if to[i][0] != to[i][1]:
            f_out.writelines('*' + str(to[i][0] // to[i][1]))
        i += to[i][0]
