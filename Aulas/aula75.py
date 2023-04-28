"""
EXERCÍCIO
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro.
"""

# def duplica(num):
#     return num * 2

# def triplica(num):
#     return num * 3

# def quadruplica(num):
#     return num * 4

# print(duplica(2))
# print(triplica(2))
# print(quadruplica(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))