# variavel array
array = ['a', 'b', 'c']

# mescla a array de letras com uma array de numeros
array.extend(range(1, 4))

for i in array:
    print(i)

print('============')

array = [4, 5, 6]

# mescla a array de numeros com uma array de letras
array = array + ['d', 'e', 'f']

for i in array:
    print(i)
