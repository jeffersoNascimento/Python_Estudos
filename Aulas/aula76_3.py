# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# setdefault - adiciona valor se a chave não existe 
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

dicionario1 = {
    'chave1': 1,
    'chave2': 2,
    'lista1': [1, 2, 3]
}
# d2 = dicionario1.copy() # shallow copy (copia rasa)
d2 = copy.deepcopy(dicionario1) # deepcopy (copia profunda)

d2['chave1'] = 100
d2['lista1'][2] = 999

print(dicionario1)
print(d2)
