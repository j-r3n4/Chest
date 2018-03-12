import os
import sys
from time import sleep

# Logo do programa!
print('-' * 41)
print('     Calculadora Simples Version 1.0')
print('-' * 41)
print('             Seja bem-vindo!')
print('-' * 41)
sleep(3)
os.system('clear')

# Valores para usar na Opção!
n1 = int(input('1# Digite um valor: '))
n2 = int(input('2# Digite um valor: '))
os.system('clear')

# Estética
print('-' * 41)
print('           Carregando Opções!')
print('-' * 41)
sleep(2)
os.system('clear')

# Var Menu(Opção!) e While do Programa!
opt = 0
while opt != 6:
    print('''       # Menu de Opções #

 [ 1 ]  +  (somar)
 [ 2 ]  x  (multiplicar)
 [ 3 ]  -  (subtrair)
 [ 4 ]  ÷  (dividir)
 [ 5 ]  CE
 [ 6 ]  ON/OFF
    ''')
    opt = float(input(' >>> Opção: '))

    if opt == 1:
        somar = n1 + n2
        os.system('clear')
        print('\nResultado: {} + {} = {}'.format(n1, n2, somar))
        sleep(5)
        os.system('clear')

    elif opt == 2:
        multiplicar = n1 * n2
        os.system('clear')
        print('\nResultado: {} x {} = {}'.format(n1, n2, multiplicar))

        sleep(5)
        os.system('clear')

    elif opt == 3:
        subtrair = n1 - n2
        os.system('clear')
        print('\nResultado: {} - {} = {}'.format(n1, n2, subtrair))
        sleep(5)
        os.system('clear')

    elif opt == 4:
        dividir = n1 / n2
        os.system('clear')
        print('\nResultado: {} ÷ {} = {:.2f}'.format(n1, n2, dividir))
        sleep(5)
        os.system('clear')

    elif opt == 5:
        os.system('clear')
        print('Informe os números novamente: ')
        n1 = float(input('\n1# Digite um valor: '))
        n2 = float(input('2# Digite um valor: '))
        os.system('clear')
        print('-' * 41)
        print('           Carregando Opções!')
        print('-' * 41)
        sleep(2)
        os.system('clear')

    elif opt == 6:
        os.system('clear')
        print('-' * 41)
        print('        Calculadora Simples - 1.0')
        print('        Finalizando, Volte sempre')
        print('-' * 41)
        sleep(5)
        sys.exit(0)

    else:
        os.system('clear')
        print('Opção inválida, Tente novamente.')
        sleep(3)
        os.system('clear')
