#Escreva um programa que leia a velocidade de um carro
# Se ele ultrapássar 80km/h, escreva uma mensagem dizendo que ele foi multado
#A multa irá custar R$7,00 para cada km acima do limite

velocidade = int(input('Diga a velocidade do carro: '))
multa = (velocidade - 80) * 7 

if velocidade <= 80:
    print ('Você estava dentro da velocidade permitida!')
else:
    print ('Você foi multado em R$ {:.2f}, R$ 7,00 para cada km acima do limite!'.format(multa))