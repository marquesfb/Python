# Curso de Programação IITC Módulo 01 - Aula 11 (23/05/2023)

# QUESTÃO: Verificar se, pela idade, o usuário pode votar e dirigir.

nome = str(input('\nQual seu nome?: '))
idade = int(input('Qual sua idade?: '))

if idade >= 18:
   print(f'\n{nome}, com {idade} anos você pode votar e dirigir! =D\n')
elif 18 > idade >= 16:
   print(f'\n{nome}, com {idade} anos você pode votar, mas não pode dirigir! xD\n')
else:
   print(f'\n{nome}, com {idade} anos você não pode votar e nem dirigir! :(\n')

# QUESTÃO: Verificar se o aluno foi aprovado

nota01 = float(input('Qual a sua nota no primeiro semestre?: '))
nota02 = float(input('Qual a sua nota no segundo semestre?: '))
MEDIA_ESCOLAR = 7 # Constantes são escritas em maiúsculo

media_aluno = (nota01 + nota02)/2

if media_aluno >= MEDIA_ESCOLAR:
    print(f'\n{nome}, você foi aprovado com {media_aluno} de média! Parabéns!')
else:
    print(f'\n{nome}, você foi reprovado com {media_aluno} de média! Estude mais!')
