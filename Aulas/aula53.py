# enumerante - enumero iteráveis (indices)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = enumerate(lista)
#lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)
#print(next(lista_enumerada))

# for a, b in enumerate(lista):
#     # a, b = i
#     print(a, b)

# print(10 * '-')

for i in enumerate(lista):
    print('for da tupla: ')
    for valor in i:
        print(f'\t{valor}')

# for i in lista_enumerada:
#     print(i)

#print('Lista enumerada: ', lista_enumerada)

