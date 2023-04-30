import copy

from dados import produtos

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos produtos por deep copy (copia profunda)
novos_produtos = [
    {**p, 'preco': round(p ['preco'] * 1.1)} 
    for p in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior ao menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print()
print(*produtos_ordenados_por_nome, sep='\n')