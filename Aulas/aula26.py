"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro
= - Força  número a aparecer depois dos zeros
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversation flags - !r !s !a
"""
var = 'ABCD'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}.')
print(f'{var:*^10}')
print(10 * '-')
print(f'{1000.123456789:.2f}')
print(f'{1000.123456789:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')

