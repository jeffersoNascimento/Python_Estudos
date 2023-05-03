# count é um iterador sem fim (contador infinito)
from itertools import count

c1 = count() # iterável e iterator
r1 = range(10) # iterável mas não é um iterator

# print('c1', hasattr(c1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))
# print('r1', hasattr(r1, '__iter__'))
# print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i > 20:
        break

    print(i)

print()
print('range')
for i in r1:
    print(i)
