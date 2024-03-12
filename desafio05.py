#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O valor digitado é: {}, o dobro dele é {}, o triplo dele é: {} e a raiz quadrada dele é: {:.1f}'.format(n, d, t, r))