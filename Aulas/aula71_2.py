"""
args - Arguments não nomeados
* - *args (empacotamento e desempacotamento)
args -> Empacota o que eu enviar pra função 
dentro de uma tupla.

"""
# Lembre-se de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args): 
    total = 0
    for numero in args:
        total += numero
    return total

soma1_3 = soma(1, 2, 3)
# print(soma1_3)
soma4_6 = soma(4, 5, 6)
# print(soma4_6)

numeros = 1, 2, 3, 4, 5, 6
outra_soma = soma(*numeros)
print(outra_soma) # desempacota uma tupla para enviar como parametros para uma função.

print(sum(numeros)) # essa linha faz a mesma soma do codigo acima

# print(sum((10, 20, 30, 40, 50))) # função "sum" faz a soma dos argumentos.