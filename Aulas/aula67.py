"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(5, 10)
soma(5, 5, 5)

