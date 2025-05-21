from random import randint
verifica = True
numeroAleatorio = int(randint(1,20))
while verifica :
    selecao = int(input('Digite um numero entre 1 e 20: '))
    if(selecao > numeroAleatorio):
        print('O seu numero é maior que o numero aleatorio')
    elif(selecao < numeroAleatorio):
        print('O seu numero é menor que o numero aleatorio')
    elif(selecao == numeroAleatorio):
        print('Você achou o numero secreto!!!')
        resposta = input('Quer jogar de novo?(S/N) ').upper()
        if(resposta == 'S'):
            numeroAleatorio = int(randint(1,20))
        elif resposta == 'N':
            verifica = False
        else:
            print('Opção incorreta!!!')