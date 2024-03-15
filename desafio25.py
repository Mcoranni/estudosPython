#Faça um programa que leia uma frase pelo teclado e mostre:
#1 - Quantas vezes aparece a letra "a"
#2 - Em que posição ela aparece a primeira vez
#3 - em que posição ela aparece pela última vez

nome = str(input('Digite uma frase: ')).upper().strip()

print ('A letra "a" aparece {} vezes na frase'.format(nome.count('A')))
print ('A primeira letra "a" aparece na posição {} da frase'.format(nome.find('A')+1))
print ('A última aparição de "A" na frase fica na posição {}'.format(nome.rfind('A')+1))