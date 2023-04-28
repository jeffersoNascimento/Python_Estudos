"""
Introdução ao desempacotamento + tuples (tuplas)
"""

#nomes = ['Maria', 'Helena', 'Jeff']

nome1, nome2, nome3 = ['Maria', 'Helena', 'Jeff']
nome1, *resto = ['Maria', 'Helena', 'Jeff']
print(nome1, resto)

