# isinstace - para saber se objeto é de deteminado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Jefferson'}]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('STR')
        item.upper
        print(item, isinstance(item, set))

    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

# rows = 6
# for i in range(1, rows):
#     print('*'* i)
