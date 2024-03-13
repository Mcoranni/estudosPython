import math

num = int(input('Digite um número '))
raiz = math.sqrt(num)

print('A raiz de {} é {}'.format(num, math.ceil(raiz)))
#Programa formatado para o resultado arredondado para cima

num2 = int(input('Digite um número '))
raiz = math.sqrt(num2)

print('A raiz de {} é {:.2f}'.format(num2, raiz))
#Programa formatado para o resultado limitado à 2 casas decimais

num3 = int(input('Digite um número '))
raiz = math.sqrt(num)

print ('A raiz de {} é {}'.format(num3, math.floor(raiz)))
#Programa formatado para o resultado arredondado para baixo

import random
num4 = random.randint(1, 200)
print ('O número que eu gerei foi {}'.format(num4))
#Programa formatado para gerar um número de 1 a 200 utilizando o import random

import emoji
print (emoji.emojize('Olá mundo 🌕'))