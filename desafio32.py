#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
num1 = int(input('Primeiro numero: '))
num2  = int(input('Segundo numero : '))
num3 = int(input('Terceiro numero: '))

# Achando o maior número
maior = num1

if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
else:
    print ('O maior é {}'.format(maior))