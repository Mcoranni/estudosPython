#Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para salários menores ou iguais, o aumento será de 15%

salario = float(input('Digite seu salário: R$ '))

porc1 = salario * 10 / 100
aumento1 = salario + porc1

porc2 = salario * 15 / 100
aumento2 = salario + porc2

if salario >= 1250:
    print ('Seu salário é R$ {:.2f} e receberá 10% de aumento, ficando assim o salário de R$ {:.2f}'.format(salario, aumento1))
else:
    print ('Seu salário é R$ {:.2f} e receberá 15% de aumento, ficando assim o salário de R$ {:.2f}'.format(salario, aumento2))

