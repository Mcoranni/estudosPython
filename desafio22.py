#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#ex: digite um número: 1834
#Unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

num = int((input('Digite um número: ')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print ('O número digitado foi {} e analisando ele, posso dizer que:'.format(num))
print ('A unidade é: {}'.format(u))
print ('A dezena é: {}'.format(d))
print ('A centena é: {}'.format(c))
print ('O milhar é: {}'.format(m))