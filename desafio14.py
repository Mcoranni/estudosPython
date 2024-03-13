#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ficou alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km rodado

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km você rodou com o carro? '))

calcdias = dias * 60
calckm = km * 0.15

final = calcdias + calckm

print ('O valor a se pagar por {} dias e {:.2f} km rodados é de R${:.2f}'.format(dias, km, final))