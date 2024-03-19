nome = str(input('Qual é o seu nome? ')).strip().capitalize()
if nome == 'Marcel':
    print ('Seja bem vindo {}, Você está autorizado!'.format(nome))
else:
    print ('Você não está autorizado a entrar, {}!'.format(nome))