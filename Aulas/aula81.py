"""
Função lambda em Python
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única 
expressão.
"""
# lista = [5, 2, 8, 1, 3, 9, 4]
# lista.sort() # coloca em ordem crescente
# lista.sort(reverse=True) # ordem decrescente
# print(lista)

lista = [
    {'nome': 'Jefferson', 'sobrenome': 'Nascimento'},
    {'nome': 'Beto', 'sobrenome': 'Cunha'},
    {'nome': 'Miguel', 'sobrenome': 'Oliveira'},
    {'nome': 'Kiko', 'sobrenome': 'Silva'},
    {'nome': 'Alysson', 'sobrenome': 'Mineiro'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=lambda item: item['nome'])

# for item in lista:
#     print(item)

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)