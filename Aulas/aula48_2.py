"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 300 # altera o valor do indice 2
# del lista[3] # deleta o indice 3
# print(lista)
# numero = lista[2]
# print(numero)
lista.append(50) # adiciona o valor ao final da lista
lista.append(60)
lista.pop() # remove o ultimo item da lista
print(lista)