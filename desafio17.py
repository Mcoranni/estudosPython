#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
ang = float(input('Ângulo: '))
rad = math.radians(ang)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print ('O ângulo de {}° o seno é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}'.format(ang, seno, cosseno, tangente))