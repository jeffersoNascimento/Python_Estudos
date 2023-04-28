# Desempacotamento em chamadas
# de nétodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda', 30, 40, 50]
tupla = 'Python', 'é', 'massa'

# a, b, *_, ultimo = lista
# print(a, ultimo)

# for nome in lista:
#     print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla)

print( 30 * '-')

salas = [
    ['Maria', 'Helena', ],
    ['Elaine', (0, 10, 20, 30, 40)],
    ['Jeff', 'João', 'Eduarda', ],
]

print(* salas, sep='\n')