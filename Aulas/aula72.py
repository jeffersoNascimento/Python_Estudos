# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor 
# da variável.
"""
Minha resolução:
def multiplica(*args): 
    total = 1
    for i in args:
        total *= i
    print(total)

multiplica(2, 2, 3, 4)
"""
def multiplica(*args): 
    total = 1
    for i in args:
        total *= i
    return total

multiplicacao = multiplica(2, 2, 3, 4)
print(multiplicacao)


# Crie uma função que fale se um número é par ou impar.
# Retorne se um número é par ou impar.
"""
Minha resolução:
def par_impar(num):
    if num % 2 == 0:
        print(f'{num} é um número par.')
    else:
        print(f'{num} é um número impar.')

par_impar(16)
print(par_impar)
"""

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(5))

