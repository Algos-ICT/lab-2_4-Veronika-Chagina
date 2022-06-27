def prefix_function(S):
    p = [0]*(len(S)+1)
    i, j = 1, 0
    while i < len(S):
        if S[i] == S[j]:
            p[i+1] = j + 1
            i += 1
            j += 1 
        else:
            if j > 0:
                j = p[j]
            else:
                p[i+1] = 0
                i += 1
    return p
def decomposition(S):
    p = prefix_function(S)
    result = []
    while len(p) != 1:
        mx_val = max(p)
        mx_ind = p.index(mx_val)
        if max(p) != 0:
            ln = mx_ind - mx_val
            mult = mx_ind // ln
            if mult > 1:
                result.append(S[:ln] + "*" + str(mult))

            else: result.append(S[:ln])
            S = S[mx_ind:]
        else:
            last = result[-1] if result else None
            if last and '*' not in last:
                result[-1] = last + S[0]
            else:
                result.append(S[0])
            S = S[1:]
        p = prefix_function(S)
    return result
with open('input.txt') as f:
    s = f.readline().strip()
decomposed = "+".join(decomposition(s))
word = decomposed if len(decomposed) < len(s) else s
print(word)
