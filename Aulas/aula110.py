# groupby - agrupamento valores (itertools)
from itertools import groupby


alunos = [
    {'nome': 'Jeff', 'nota': 'A'},
    {'nome': 'Lilian', 'nota': 'B'},
    {'nome': 'Lívia', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Fabrício', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Dudu', 'nota': 'A'},
    {'nome': 'André', 'nota': 'B'},
    {'nome': 'Anderson', 'nota': 'C'},
]
alunos_agrupados = sorted(alunos, key=lambda a: a['nota']) # ordena por nota
grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# alunos = ['a', 'a', 'a', 'a', 'b', 'c']
# grupos = groupby(alunos)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))