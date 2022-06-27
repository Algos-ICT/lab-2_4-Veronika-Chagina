import random
import time

t_start = time.perf_counter()
def PolyHash(P, l, p, x):
    result = 0
    for i in reversed(range(l)):
        result = (result * x + ord(P[i])) % p
    return result % p


def PrecomputeHashes(T, l, k, p, x):
    H = [0] * (l - k + 1)
    S = T[l - k: l]
    H[l - k] = PolyHash(S, k, p, x)
    y = 1
    for i in range(1, k + 1):
        y = (y * x) % p
    for i in range(l - k - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + k]) + p) % p
    return H


with open('input.txt', 'r') as f:
        text = f.readline().strip()
        text_length = len(text)
        request = int(f.readline())
        p = 10 ** 9 + 7
        x = random.randint(1, p - 1)
        for i in range(request):
            a, b, l = map(int, f.readline().split())
            H = PrecomputeHashes(text, text_length, l, p, x)
            if H[a] == H[b]:
                print('Yes')
            else:
                print('No')


print('Время работы: %s секунд' % (time.perf_counter() - t_start))
