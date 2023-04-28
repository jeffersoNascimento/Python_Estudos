# raise - lamçando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você não pode dividir um número por zero!')
    return True

def int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" é {tipo_n.__name__} você deve digitar int ou float.'
        )
    return True 

def divide(n, d):
    int_ou_float(n)
    int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))


# def divide(n, d):
    # try:
    #     return n / d
    # except ZeroDivisionError:
    #     print('ACONTECEU UM ERRO:')
    #     raise
#     if d == 0:
#         raise ZeroDivisionError('Você não pode dividir um número por zero')
    
#     return n / d
    
# print(divide(8, 0))