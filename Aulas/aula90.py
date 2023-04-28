import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # iterable.__iter__() -> tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))

# for i in iterator:
#     print(i)

lista = [n for n in range(10000)]
generator = (n for n in range(10000)) # generator usa () | ocupa menos espaço na memória

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))



