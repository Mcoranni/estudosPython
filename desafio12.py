#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Olá, digite seu salário? '))

calculo = (salario * 15) / 100

resultado = salario + calculo

print ('Você recebeu um aumento de 15% e seu salário passará a ser R${:.2f}'.format(resultado))