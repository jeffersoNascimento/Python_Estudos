"""
Interpolação básica de strings
s - string
d ou i - int
f - float
x ou X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

#HEXADECIMAL    
print('O hexadecimal de %i é %04x' % (15, 15))