"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_ = frase.split()
#lista = frase.split(',')
lista = []

for i, frase in enumerate(lista):
    lista.append(lista_[i].strip())
    # print(lista[i].strip())
    # print(lista[i].rstrip())
    # print(lista[i].lstrip())

# print(lista)
# print(lista_)

frases_unidas = '-'.join(lista_)
print(frases_unidas)

