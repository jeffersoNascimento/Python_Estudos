# Introdução às Generator functions em Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

# def generator(n=0):
#     yield 1 # pausar
#     print('Continuando...')
#     yield 2 # pausar
#     print('Mais uma...')
#     yield 3
#     print('Terminar')
#     return 'Acabou'

gen = generator(n=0)
# print(gen.__iter__())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for n in gen:
    print(n)