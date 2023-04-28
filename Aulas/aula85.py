# List comprehension em Python
# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

lista = [(x, y) for x in range(3) for y in range(3)]
lista = [
    [ x for y in range(3)] 
    for x in range(3)
]
print(lista)

# Eu criei um vídeo gratuito falando muito mais sobre list
# comprehension tirando como base as dúvidas desse curso.
# Veja em https://youtu.be/1YbTDczvqco