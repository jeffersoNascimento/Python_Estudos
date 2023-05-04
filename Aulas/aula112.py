# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.20},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# p_maior_que_dez = [
#     p for p in produtos
#     if p['preco'] > 10
# ]
p_maior_que_dez = filter(
    lambda p: p['preco'] > 10,
    produtos
)

print_iter(produtos)
print_iter(p_maior_que_dez)