#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Olá, me diga quanto de dinheiro você tem: R$'))

dolar = din/4.98
euro = din/5.43

print ('Com: R${:.2f} Reais e pode comprar U${:.2f} Dólares e €{:.2f} Euros'.format(din, dolar, euro))