with open("input.txt", 'r') as f:
    pattern = f.readline().rstrip()
    text = f.readline()
pattern_length, text_length = len(pattern), len(text)


def PolyHash(pat, p, x):
    result = 0
    for i in reversed(range(pattern_length)):
        result = (result * x + ord(pat[i])) % p
    return result % p


def PrecomputeHashes(T, p, x):
    global pattern_length, text_length
    H = [0] * (text_length - pattern_length + 1)
    S = T[text_length - pattern_length: text_length]
    H[text_length - pattern_length] = PolyHash(S, p, x)
    y = 1
    for i in range(1, pattern_length + 1):
        y = (y * x) % p
    for i in range(text_length - pattern_length - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + pattern_length]) + p) % p
    return H


def Rabin_Karp(pattern, text):
    global pattern_length, text_length
    p = 10 ** 9 + 9
    x = 127
    count = 0
    result = []
    hash_pattern = PolyHash(pattern, p, x)
    hash_string = PrecomputeHashes(text, p, x)
    for i in range(text_length - pattern_length + 1):
        if hash_pattern != hash_string[i]:
            continue
        count += 1
        result.append(str(i + 1))
    print(str(count) + "\n" + " ".join(result))


Rabin_Karp(pattern, text)
