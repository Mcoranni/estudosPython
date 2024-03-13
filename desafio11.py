#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Olá, qual o preço do produto? '))

calculo = preco * 5 / 100

resultado = preco - calculo

print ('Olá, a loja está com 5% de desconto e o produto ficará por R${:.2f}'.format(resultado))