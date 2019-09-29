# variavel string
author = 'Bruno Silva'
print(author)

# outra variavel string
upper_case = author.upper()

print(upper_case)

# variavel objeto
data = {'first': 'Primeiro', 'middle': 'Meio', 'last': 'Ultimo'}

# variavel string formatada
# note o uso de 'splat' (**data)
# algo semelhante ao spread do JavaScript
template = '{first} {last}'.format(**data)

print(template)
