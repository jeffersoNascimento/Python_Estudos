"""
Exercício
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Judas')

indices = range(len(lista))

for i in indices:
    print(i, lista[i])