#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Olá, me diga quanto de dinheiro você tem: '))

conversao = din/4.98

resultado = conversao

print ('Olá, você tem: R${:.2f} Reais e pode comprar ${:.2f} Dólares'.format(din, resultado))