n1 = input('Olá, digite alguma coisa: ')

print ('O tipo primitivo desse valor é ', type(n1))
print ('Só tem espaços? {}'.format(n1.isspace()))
print ('É um número? {}'.format(n1.isnumeric()))
print ('Está em caixa alta? {}'.format(n1.isupper()))
print ('Está em caixa baixa? {}'.format(n1.islower()))