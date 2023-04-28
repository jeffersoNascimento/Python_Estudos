"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

num = input('Dobrar número: ')

try:
    print('Str: ', num) #fail fast
    num_float = float(num)
    print('Float: ', num_float)
    print(f'O dobro de {num} é {num_float * 2:.2f}')
except:
    print('Isso não é um número!')

# if num.isdigit():
#     num_float = float(num)
#     print(f'O dobro de {num} é {num_float * 2:.2f}')
# else:
#     print('Isso não é um número!')