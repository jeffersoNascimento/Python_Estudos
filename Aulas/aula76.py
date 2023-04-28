"""
Dicionários em Python (tipo dict)
Dicionários são extruturas de dados do tipo
par de "chave" e 'valor'.
Chaves podem ser consideradas como 'índice'
que vimos na lista e podem ser tipos imutáveis
como: str, int, float, boll, tuple, etc.
o valor pode ser de qualduer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple.
Multável: dict, list.
pessoa = {
     'nome': 'Jeff',
     'sobrenome': 'Nascimento'
     'idade': 32
     'altura': 1.75
     'endereços': [
         {'rua': 'tal', 'número': 123456}
         {'rua': 'outra rua', 'número': 654321}  
     ]     
}
"""
pessoa = {
    'nome': 'Jeff',
    'sobrenome': 'Nascimento',
    'idade': 32,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal', 'número': 123456},
        {'rua': 'outra rua', 'número': 654321}, 
    ],
}
# pessoa = dict(nome= 'Jeff',sobrenome= 'Nascimento')
print(pessoa, type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])
