#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa

#1 - Ler o comprimento do cateto oposto
#2 - Ler o comprimento do cateto adjacente de um triangulo retangulo
#3 - Calcular e mostrar o comprimento da hipotenusa

import math
oposto = float(input('Digite o comprimento do Cateto Oposto: cm '))
adj = float(input('Digite o comprimento do Cateto Adjacente cm '))

somacatetos = (oposto**2) + (adj**2)
hip = math.sqrt(somacatetos)
#Acima a minha solução, antes de ver a resposta do professor

print ('A hipotenusa tem o comprimento de {:.2f}cm'.format(hip))

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)

print ('A hipotenusa vai medir {:.2f}'.format(hi))
#Acima a solução apresentada pelo professor