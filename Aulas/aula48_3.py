"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.pop()
lista.append('Jeff')
del lista[-1] # remove ultimo item da lista
# lista.clear()
lista.insert(0, 5)
lista.insert(4, 'Nascimento')

print(lista)
