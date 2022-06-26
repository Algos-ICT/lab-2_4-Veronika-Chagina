with open('input.txt') as f:
    text = f.readline()


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


answer = prefix_function(text)
print(answer)
