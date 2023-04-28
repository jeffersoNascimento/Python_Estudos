# Módulos do padrão Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
print(sys.platform)
sys.exit() # sai do programa
print('Não vai aparecer pq vem depois do exit()')

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do módulo
# from sys import exit, platform

# platform = 'Minha plataforma'

# print(platform)
# exit()
# print(123456)


# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)
# ex()
# print(321)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má pratica - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import * # má prática

# print(platform)
# exit()
# print('Não vai aparecer pq vem depois do exit()')