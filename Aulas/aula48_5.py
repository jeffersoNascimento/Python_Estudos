"""
Cuidados com dados mutáveis
= - copia o valor (imutáveis)
= - aponta para o mesmo valor na memória (multável)
"""
lista_a = ['Jeff', 'Nascimento'] 
lista_b = lista_a.copy()

lista_a[1] = 'Silva'
print(lista_a, lista_b)
