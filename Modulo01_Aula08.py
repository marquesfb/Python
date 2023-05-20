# Aula 08 Input > Process > Output

boas_vindas = '\nOlá! Seja bem vindo!'
print(boas_vindas)

temperatura = float(input('Qual a temperatura hoje? '))
resposta = f'Tem certeza que a temperatura é {temperatura}ºC?'
print(resposta)

temperatura_fria = float(5)
clima_frio = None

if temperatura <= temperatura_fria:
    clima_frio = True
else:
    clima_frio = False

if clima_frio:
    print('Tá frio mesmo!')
else:
    print('Ah, nem tá frio!')