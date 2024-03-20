#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo

ret1 = float(input('Digite o comprimento da primeira reta: '))
ret2 = float(input('Digite o comprimento da segunda reta: '))
ret3 = float(input('Digite o comprimento da terceira reta: '))

if (ret1 == ret2 and ret2 == ret3):
    print ('Com essas medidas, criaremos um Triângulo Equilátero')
else:
    print ('Não podemos criar um triângulo')