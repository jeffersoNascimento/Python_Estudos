"""
args - Arguments não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        print('Soma', total, '+', numero)
        total = total + numero
        print('Total=', total)
    print(total)

soma(1, 2, 3, 4, 5, 6)