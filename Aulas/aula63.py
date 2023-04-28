"""
POSSÍVEIS PROBLEMAS E SOLUÇÕES PARA NOSSO ALGORITMO DO CPF
"""
import re
import sys
# cpf_usuario = '746.824.890-70'\
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('Digite CPF: ')
cpf_usuario = re.sub(
    r'[^0-9]', 
    '', 
    entrada
)

primeiro_caractere = entrada == entrada[0] * len(entrada)

# if primeiro_caractere:
#     print('Você enviou dados sequênciais.')
#     sys.exit()

nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for i in nove_digitos:
    resultado_digito_1 += int(i) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for i in dez_digitos:
    resultado_digito_2 += int(i) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == cpf_calculo:
    print(f'{cpf_usuario} é válido')
else:
    print('CPF inválido')




