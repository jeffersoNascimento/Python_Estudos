""" QUESTÃO 1
Faça um programa que peça ao usuário para digitar um número interiro, 
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

if num.isdigit():
    print('Inteiro')
else:
    print('Não é um número inteiro')

num_int = int(num)
num_par_impar = num_int % 2


if num_par_impar == 0:
    print(f'O número {num_int} é par')
else:
    print(f'O número {num_int} é impar')



# SOLUÇÃO 1 DO PROFESSOR
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro.')

# SOLUÇÃO 2 DO PROFESSOR
# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro.')



""" QUESTÃO 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boatarde 12 - 17 e Boa noite 18 - 23.
"""
print('Digite a hora com números inteiros por favor.')
hora = input('Que horas? ')

if hora.isdigit():
    print('')
else:
    print('Ops, algo deu errado!')

hora_int = int(hora)

if hora_int < 12:
    print('Bom dia!')
elif hora_int >= 12 and hora_int < 18:
    print('Boa tarde!')
elif hora_int >= 18 and hora_int <= 24:
    print('Boa noite!')
else:
    print('Digite uma hora válida.')



# SOLUÇÃO DO PROFESSOR
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora.')
# except:
#     print('Por favor, digite apenas números inteiros')



""" QUESTÃO 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver enre 5 a 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande" 
"""

# nome = input('Digite seu primeiro nome: ')

# if len(nome) <= 4:
#     print('Seu nome é curto')
# elif len(nome) > 4 and len(nome) <= 6:
#     print('Seu nome é normal') 
# elif len(nome) > 6:
#     print('Seu nome é muito grande')



# SOLUÇÃO DO PROFESSOR
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')

