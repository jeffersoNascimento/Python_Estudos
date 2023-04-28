# Dicionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dicionario = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    # if chave == 'categodia'
}

print(*dicionario, sep=' - ')

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: valor 
    for chave, valor in lista
}

print(*dc, sep='\n')
print(dict(dc))

