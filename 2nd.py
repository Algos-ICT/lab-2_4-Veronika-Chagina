with open('input.txt', 'r') as f:
    message = f.readline().replace(' ', '')
    length_of_message = len(message)

prefix = [dict() for i in range(length_of_message)]
suffix = dict()
prefix[0][message[0]] = 1

for i in range (1, length_of_message):
    prefix[i] = prefix[i -1].copy()
    prefix[i][message[i]] = prefix[i].get(message[i], 0) + 1
suffix[message[length_of_message-1]] = 1
answer = 0

for i in range(length_of_message - 2, 0, -1):
    for k in prefix[i-1].keys():
        answer += prefix[i-1][k] * suffix.get(k, 0)
    suffix[message[i]] = suffix.get(message[i], 0) + 1
print(answer)


with open('output.txt', 'w') as f_out:
    f_out.write(str(answer))