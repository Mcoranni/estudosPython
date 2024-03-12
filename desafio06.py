#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
n1 = float(input('Digite sua nota do primeiro semestre: '))
n2 = float(input('Agora digite a sua nota do segundo semestre: '))

notas = int(n1 + n2)
final = notas / 2

print ('A média entre {} e {} é {}'.format(n1, n2, final))
