#Escreva um programa que converta uma temperatura digitada em °c para °f

temp = float(input('Me informe a temperatura atual: °c '))

conversao = temp * 1.8 + 32

print ('Convertendo {}°C, nós temos {:.1f}°F'.format(temp, conversao))