#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar adivinhar qual foi o número escolhido pelo computador
#O computador deverá escrever na tela se o usuário venceu ou perdeu

import random
num = int(input('Pensei em um número de 0 a 9, tente adivinhar qual foi! '))
comp = random.randint(0,9)

if num == comp:
    print ('Parabéns, pensei exatamente no número {}'.format(comp))
else:
    print ('Que pena, o número que pensei foi {}'.format(comp))