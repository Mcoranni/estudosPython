n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

if m >= 7.0:
    print ('Sua média foi {:.1f}. PARABÉNS, você está APROVADO'.format(m))
else:
    print ('Sua média foi {:.1f} Que pena, você está REPROVADO'.format(m))