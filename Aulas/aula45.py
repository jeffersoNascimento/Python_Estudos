"""
COMO O for FUNCIONA (__iter__)
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# #texto = 'jeff'.__iter__()
# texto = iter('jeff')
# print(texto)
# print(texto.__next__()) # ou print(next(texto))
# print(texto.__next__()) 
# print(next(texto)) 
# print(texto.__next__())
# #print(texto.__next__()) Quando acaba o valor aparece um ERRO StopIteration

# for letra in texto
texto = 'jeff' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break


