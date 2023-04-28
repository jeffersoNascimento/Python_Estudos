"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Jeff Nascimento'
outra_variavel = f'{string[:4]}_{string[4:]}' # Altera o nome
# string[4] = '_' -> ERRO
# print(string)
# print(outra_variavel)
# print(len(string), len(outra_variavel))
print(string.capitalize()) # Coloca a primeira letra maiúscula
print(string.zfill(20)) # Aumenta os caracteres acrescentando zeros a esquerda
