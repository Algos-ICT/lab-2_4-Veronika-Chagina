def prefix_function(text):
    p = [0 for a in range(len(text) - 1)]
    i, j = 1, 0
    while i < len(text)-1:
        if text[i] == text[j]:
            p[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = p[j-1]
        else:
            p[i] = 0
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
