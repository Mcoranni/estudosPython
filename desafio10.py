#Fazer um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária para pintá-la
#Vamos usar como base de calculo "Cada litro de tinta, pinta 2m²"

largura = float(input('Me diga a largura da parede: '))
altura = float(input('Me dia a altura da parede: '))
demaos = int(input('Me diga quantas demãos você precisa: '))

area = largura * altura
tinta = 2

quantidade = (area * demaos / tinta)

print ('Para pintar uma área de {}, você precisará de {:.0f} litros de tinta'.format(area, quantidade))