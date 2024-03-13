#O professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem aleatória
import random

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print ('A ordem de apresentação será: {}'.format(lista))