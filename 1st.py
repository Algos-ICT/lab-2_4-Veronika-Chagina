with open('input.txt', 'r') as f:
    substring = f.readline().rstrip()
    string = f.readline().rstrip()

n_sub = len(substring)
n_string = len(string)

match = []

for i in range(n_string):
    if string[i] == substring[0]:
        if i + n_sub <= n_string:
            if string[i:i + n_sub] == substring:
                match.append(str(i + 1))
                i += n_sub

with open('output.txt', 'w') as f_out:
    f_out.write(str(len(match)) + '\n')
    f_out.write(' '.join(match))
