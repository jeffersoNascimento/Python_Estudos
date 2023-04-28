"""
Argumentos nomeados e não nomeados em funções de Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y):
    print(f'{x=} + {y=} =', x + y)

soma(10, 20)
soma(11, 2)