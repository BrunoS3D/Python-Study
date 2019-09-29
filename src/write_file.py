file = open('helloworld.txt', 'w+')

file.write('file: helloworld.txt\n\n')

for y in range(10):
    line = ''
    if y == 0:
        line = 'y | x\n'

    for x in range(10):
        if x == 0:
            line += f'{y} | '

        line += x.__str__() + ' '

    file.write(line + '\n')

file.close()
