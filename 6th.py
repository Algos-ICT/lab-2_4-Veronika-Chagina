def count_z_func(s, n, z):
    ans = []
    l, r = -1, -1
    for i in range(1, n-1):
        if i < r:
            z[i] = min(z[i - l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        ans.append(z[i])

    return " ".join(list(map(str, ans)))


with open('input.txt', 'r') as f_in:
    s = f_in.readline()
    n = len(s)
    z = [0] * n

with open('output.txt', 'w') as f_out:
    res = count_z_func(s, n, z)
    f_out.write(res)
