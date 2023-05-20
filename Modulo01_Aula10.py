# Curso de Programação IITC Módulo 01 - Aula 10 (18/05/2023)

# QUESTÃO: Verficar se o número digitado é positivo, negativo ou zero.

"""num = None

while True:
    try:
        num = float(input('\nDigite um número: '))
        if num == 0:
            print(f'{num} é nulo.')
        elif num > 0:
            print(f'{num} é positivo.')
        else:
            print(f'{num} é negativo')
        break
    except ValueError:
        print('Esse não é um número válido.')
        continue
"""

# QUESTÃO: Pedra, papel, tesoura!

import random
import time

jogador = None
aleatorio = None
pc = None
vencedor = None

while True:
    try:
        jogador = str(input('\nPedra, papel ou tesoura?: ')).lower()
        if not (jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura'):
            raise ValueError
        break
    except ValueError:
        print('Opção inválida.')
        continue

print('\nJo..')
time.sleep(0.5)
print('Ken..')
time.sleep(0.5)
print('Po!')



aleatorio = random.randint(1,3)

if aleatorio == 1:
    pc = 'pedra'
elif aleatorio == 2:
    pc = 'papel'
else:
    pc = 'tesoura'

if jogador == pc:
    vencedor = 'Ninguém'

elif jogador == 'pedra' and pc == 'tesoura':
    vencedor = 'Jogador'

elif jogador == 'papel' and pc == 'pedra':
    vencedor = 'Jogador'

elif jogador == 'tesoura' and pc == 'papel':
    vencedor = 'Jogador'

else:
    vencedor = 'Computador'

print(f"""
Jogador: {jogador}
Computador: {pc}

{vencedor} venceu a rodada!""")