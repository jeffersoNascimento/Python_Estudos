# Combinations, Permutados e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino'],
]

print_iter(product(*camisetas))
print()
print_iter(combinations(pessoas, 2)) # grupo de dois
print('-' * 20)
# print_iter(combinations(pessoas, 3)) # grupo de três...
print_iter(permutations(pessoas, 2))