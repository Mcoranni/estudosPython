#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Olá, me fale a largura da parede que deseja pintar '))
altura = float(input('Agora me diga a altura da parede '))
demaos = float(input('Agora me diga quantas demãos você irá passar na parede '))

area = largura * altura
lata = 2

quantidade = (area * demaos / lata)

print('Você tem uma área de {:.1f}m² e precisará de {:.0f} demãos de tinta '.format(area, demaos))
print ('Para píntar uma parede de {:.1f}m², você irá precisar de {:.0f} litros de tinta.'.format(area, quantidade))