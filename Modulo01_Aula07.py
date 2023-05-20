# Desafio Aula 07
import time

# ------------ VAI CHOVER? -------------------

sair = None
chuva = None
guarda_chuva = None

def pega_guarda_chuva(chuva):
    if chuva == 'S':
        guarda_chuva = bool(True)
    else:
        guarda_chuva = bool(False)
    return guarda_chuva

print('\nVocê está em seu quarto e lembrou que tem um compromisso.')
time.sleep(2)
print('Você está saindo e sua mãe te chama...\n')
time.sleep(1)

while True:
    try:
        sair = str(input('- Vai sair? [S/N]: ')).upper()
        if sair == 'N':
            print('- Ah, ok! Me avise se for sair.\n')
            time.sleep(1)
            exit('Você voltou para seu quarto.')
        elif sair == 'S':
            print('- Ah, então resolveu sair do seu quarto!\n')
        else:
            raise ValueError
        break
    except ValueError:
        print('Não entendi o que você disse.\n')
        continue

while True:
    try:
        chuva = str(input('- Está chovendo? [S/N]: ')).upper()
        if (chuva != 'S') and (chuva != 'N'):
            raise ValueError
        break
    except ValueError:
        print('- Não entendi..\n')
        continue

guarda_chuva = pega_guarda_chuva(chuva)

if guarda_chuva == False:
        while True:
            try:
                print('- Acho que vai chover mais tarde.')
                time.sleep(1)
                chuva = str(input('\n- Não acha melhor levar o guarda-chuva? [S/N]: ')).upper()
                if (chuva != 'S') and (chuva != 'N'):
                    raise ValueError
                break
            except ValueError:
                print('- Não entendi..\n')
            continue

guarda_chuva = pega_guarda_chuva(chuva)

if guarda_chuva:
    print('- Então, leve o guarda-chuva!\n')
    msg = str('com')
else:
    print('- Tá bom..então não precisa levar o guarda-chuva.\n')
    msg = str('sem')

time.sleep(1)
print(f'Você saiu de casa {msg} seu guarda-chuvas.')
time.sleep(2)

#------------ O QUE SIGNIFICA ESSA COR? -----------------

cor = None

print('\nVocê está indo a pé se matricular no curso de Python do IITC a poucas quadras de casa.')
time.sleep(3)

print('Você chegou a um cruzamento e percebe que o semáforo mudou de cor.\n')
time.sleep(2)

print('Uma senhora se aproxima e diz...\n')
time.sleep(2)

print('- Não enxergo muito bem...')
time.sleep(1)

while True:
    try:
        cor = str(input('- Qual cor está o semáforo? ')).upper()
        time.sleep(1)
        if cor == 'VERDE':
            print('\n- Temos que esperar...')
            time.sleep(1)
            print('Ela parece impaciente...\n')
            continue
        elif cor == 'AMARELO':
            print('\n- Atenção...')
            time.sleep(1)
            print('Ela se agarra ao seu braço como se preparasse para algo importante...\n')
            continue
        elif cor == 'VERMELHO':
            print('\n- Os carros pararam!')
            time.sleep(1)
            print('- Vamos! Me ajude a atravessar!\n')
        else:
            raise ValueError
        break
    except ValueError:
        print('Por um momento você pensa que isso não parece certo...\n')
        time.sleep(1)
        continue

time.sleep(3)

if guarda_chuva:
    print('Você se atrapalha um pouco por causa do guarda-chuvas, mas consegue ajudar à senhora a atravessar a rua.\n')
else:
    print('Você ajuda a senhora a atravessar a rua sem problemas.\n')

time.sleep(3)

# MAIS, OU MENOS?

fichas = None
operacao = None
quantidade = None

print('Você chegou ao local de inscrição para o curso.')
time.sleep(1)
print('Parece que seus amigos vão se atrasar...\n')
time.sleep(3)
print('Você resolve pedir umas fichas de inscrição para eles..')
time.sleep(2)

print('- O senhor poderia me dar umas fichas extras, para meus amigos? Você pergunta.\n')
time.sleep(3)

print('- Claro!')
while True:
    try:
        fichas = int(input('- Quantas fichas extras você quer? '))
        if fichas == 0:
            print('- Seus amigos não podem se inscrever sem uma ficha!\n')
            time.sleep(1)
            continue
        if fichas <0:
            raise ValueError
        break
    except ValueError:
        print('- Desculpe, não entendi...\n')
        continue

fichas = fichas +1

print(f'- Aqui estão as suas {fichas} fichas de inscrição.\n')
time.sleep(3)

print('Você pegou as fichas e percebeu que fez a conta errada...\n')
time. sleep(1)

while True:
    try:
        operacao = str(input('- Você precisa de mais, ou menos fichas? ')).lower()
        time.sleep(2)
        if not (operacao == 'mais' or operacao == 'menos'):
            raise ValueError
        break
    except ValueError:
        print('- Não entendi o que você disse...\n')
        continue

while True:
    try:
        quantidade = int(input(f'- Quantos a {operacao}? '))
        if ((operacao == 'menos') and (quantidade >= fichas)) or (quantidade <= 0):
            print('- Eu acho que você não fez essa conta direito...\n')
            time.sleep(1)
            continue
        break
    except ValueError:
        print('Eu realmente não te entendi...\n')
        time.sleep(1)
        continue

if operacao == 'mais':
    fichas = fichas + quantidade
else:
    fichas = fichas - quantidade

print('- Ok!')
time.sleep(2)

if fichas == 1:
    print(f'\nPor fim, você está levando {fichas} ficha de inscrição, para você apenas.\n')
    time.sleep(5)
else:
    print(f'\nPor fim, você está levando {fichas} fichas de inscrição, para você e seus amigos.\n')
    time.sleep(5)

print('Você está prestes a sair da loja e começa a chover!!!')
time.sleep(1)

if guarda_chuva:
    print('Você pensa: "Ainda bem que trouxe meu guarda-chuva!"\n')
    time.sleep(1)
    exit('Você chega em casa e agradece sua mãe por lembrar do guarda-chuva!')
else:
    print('Você pensa: "Deveria ter escutado minha mãe e trazer o guarda-chuva..."\n')
    time.sleep(1)
    exit('Você chegou em casa encharcado.')

