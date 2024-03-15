#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1 - O nome com todas as letras maiúsculas
#2 - O nome com todas minúsculas
#3 - Quantas letras ao todo (sem considerar espaços)
#4 - Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')


print ('Caixa Alta: {}'.format(nome.upper()))
print ('Caixa Baixa: {}'.format(nome.lower()))
print ('Sem espaços fica com {} caracteres.'.format(len(nome.replace(' ', ''))))
print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))