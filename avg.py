aa = {'b' : 0, 'c' : 3}

aa['d'] = 6

print(aa['d'])

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