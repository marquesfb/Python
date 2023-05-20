# Aula 05 do Curso de Programação Módulo 01
import time
from datetime import date

# Setando as variáveis
hoje = date.today()
while True:
    try:
        nasc_d = int(input('Qual dia você nasceu?: '))
        nasc_m = int(input('Qual mês?: '))
        nasc_ano = int(input('Qual ano?: '))
        nascimento = date(nasc_ano, nasc_m, nasc_d)
        break
    except ValueError:
        print('Por favor, digite uma data válida.')
        continue

# Informando ao usuário o nascimento digitado no padrão BR
nascimento_br = nascimento.strftime("%d/%m/%Y")
print(f'Você nasceu em {nascimento_br}!')

time.sleep(1)
print('Humm...')
time.sleep(2)

# Calculando a idade
idade = int(((hoje-nascimento).days+1)/365.2425)
if idade > 1:
    msg = 'anos'
else:
    msg = 'ano'
print(f'Você tem {idade} {msg}!')