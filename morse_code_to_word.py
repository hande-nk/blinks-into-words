end = []
m_c = [
    ['.', '-', None, None],
    ['-', '.', '.', '.'],
    ['-', '.', '-', '.'],
    ['-', '.', '.', None],
    ['.', None, None, None],
    ['.', '.', '-', '.'],
    ['-', '-', '.', None],
    ['.', '.', '.', '.'],
    ['.', '.', None, None],
    ['.', '-', '-', '-'],
    ['-', '.', '-', None],
    ['.', '-', '.', '.'],
    ['-', '-', None, None],
    ['-', '.', None, None],
    ['-', '-', '-', None],
    ['.', '-', '-', '.'],
    ['-', '-', '.', '-'],
    ['.', '-', '.', None],
    ['.', '.', '.', None],
    ['-', None, None, None],
    ['.', '.', '-', None],
    ['.', '.', '.', '-'],
    ['.', '-', '-', None],
    ['-', '.', '.', '-'],
    ['-', '.', '-', '-'],
    ['-', '-', '.', '.'],
]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

count = 0
for char in counter:
    print(char, end='')
    if char == 's':
        count += 1

blinks = [[None] * 4 for _ in range(count + 1)]
word, letter = 0, 0
for char in counter:
    if char != 's':
        blinks[word][letter] = char
        letter += 1
    else:
        word += 1
        letter = 0

for i in range(count + 1):
    for j in range(4):
        print(blinks[i][j], end='')
    print('')

for i in range(len(blinks)):
    for j in range(26):
        match = True
        for x in range(4):
            if blinks[i][x] != m_c[j][x]:
                match = False
                break
        if match:
            end.append(alphabet[j])
            break

for char in end:
    print(char, end='')
