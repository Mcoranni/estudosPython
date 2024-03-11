#Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros
n = float(input('Digite quantos metros² tem seu terreno: '))

print('Seu terreno tem: {:.0f}m², {:.0f} cm e {:.0f} mm'.format(n, n*100, n*1000))