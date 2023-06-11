test = {'b': 0, 'c': 3, 'd': 6}

print(test['d'])

inp = ''
result = []
while True:
    inp = input()
    if inp == 's': break
    result.append(float(inp))

res = 0

for x in result:
    res += x

print(res / len(result))
