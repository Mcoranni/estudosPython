#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

num = int(input('Digite um número: '))
if num % 2 == 0: #Todo número par é perfeitamente dividido por 2, então usamos o operador %
    #Para nos dar o resto da divisão e se o resultado for = 0, ele é par.
    print ('Esse número é par!')
else: #Caso contrário, ele será ímpar!
    print ('Esse número é impar!')