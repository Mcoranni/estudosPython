#Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros
n = float(input('Digite quantos metros² tem seu terreno: '))
km = n / 1000
hm = n * 100
dam = n * 10
dm = n / 10
cm = n * 100
mm = n * 1000

print('Seu terreno tem: {}m²'.format(n))
print('Isso equivale a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))