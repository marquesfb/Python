# Aula 09 - Módulo I do Curso de Programação do IITC


# Questão do Semáforo:

cor = None

print('\nUhm, um semáforo à frente...')
cor = str(input('Qual cor está o sinal? ')).lower()

if cor == 'verde':
    print('\nAh, podemos seguir!')
elif cor == 'amarelo':
    print('\nOpa, atenção!')
elif cor == 'vermelho':
    print('\nPARE!')
else:
    print('\nSerá daltonismo?...')


# Questão do Guarda-Chuva

chovendo = None
previsao_chuva = None
guarda_chuva = None

chovendo = str(input('\nEstá chovendo? (sim/não): ')).lower()
if chovendo == 'sim':
    guarda_chuva = True
elif chovendo == 'não':
    previsao_chuva = str(input('A previsão é de chuva? (sim/não): ')).lower()
    if previsao_chuva == 'sim':
        guarda_chuva = True
    elif previsao_chuva == 'não':
        guarda_chuva = False
    else:
        exit('Não entendi...')
else:
    exit('Não entendi...')

if guarda_chuva:
    print('\nEntão, leve o guarda-chuva!')
else:
    print('\nEntão, não precisa levar o guarda-chuva!')


# Questão da Operação Matemática

num_01 = None
num_02 = None
soma = None
subtracao = None

num_01 = int(input('\nQual o primeiro número?: '))
num_02 = int(input('Qual o segundo número?: '))

soma = num_01 + num_02
print(f'\nO resultado da soma é * {soma} *!')

subtracao = num_01 - num_02
print(f'O resultado da subtração é * {subtracao} *!')