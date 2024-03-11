#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
media1 = int(input('Digite sua nota do primeiro semestre: '))
media2 = int(input('Agora digite a sua nota do segundo semestre: '))

total = int(media1 + media2)

print ('Sua média final foi de: {}'.format(total/2))
