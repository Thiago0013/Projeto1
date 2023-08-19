from time import sleep
import os
import datetime
tempo = datetime.date.today()
nome = 'Saldo.txt'
def Depositar():
    with open(nome,'r') as arquivo:
        saldo = float(arquivo.read())
    print(saldo)
    print('-' * 60)
    deposito = float(input('Deposite R$:'))
    print('Depositando...')
    sleep(2)
    saldonovo = saldo + deposito
    with open(nome, 'w') as arquivo:
        arquivo.write(str(saldonovo))
    print(f'R$:{deposito} foi depositado!')
    print('-' * 60)
    sleep(1)
def Saldo():
    with open(nome,'r') as arquivo:
        saldo = float(arquivo.read())
    print('-' * 60)
    print(f'Seu saldo é de R${saldo}')
    print('-' * 60)
    sleep(5)
def Retirar():
    with open(nome,'r') as arquivo:
        saldo = float(arquivo.read())
    print('-' * 60)
    while True:
        retirar = float(input('Retirar R$:'))
        if retirar > saldo:
            print(f'Você quer retirar R$:{retirar} e você tem R$:{saldo}!')
            print(f'Retire uma quantidade igual ou menor do seu saldo!')
        else:
            saldonovo = saldo - retirar
            break
    with open(nome, 'w') as arquivo:
        arquivo.write(str(saldonovo))
    print(f'R$:{retirar} foi retirado!')
    print('-' * 60)
    sleep(2)
if not os.path.exists(nome):
    saldo = 0
    with open(nome, 'w') as arquivo:
        arquivo.write(str(saldo))
while True:
    print('=-' * 13, end='')
    print("MENU", end='')
    print('=-' * 14)
    print('[1] Depositar')
    print('[2] Retirar')
    print('[3] Ver Saldo atual')
    print('[4] Sair do programa')
    print('=-' * 24,end='')
    print(f'{tempo}')
    pergunta = input('Escolha: ')
    print('=-' * 30)
    if pergunta.isnumeric() == True:
        pergunta = int(pergunta)
        if pergunta == 1: 
            Depositar()
        elif pergunta == 2:
            Retirar()
        elif pergunta == 3:
            Saldo()
        elif pergunta == 4:
            print('Saindo...')
            sleep(3)
            print('Até a proxima!!!')
            break
        else:
            print('Digite um numero que o menu mostra!')