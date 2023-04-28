"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Hello, world!'
print(variavel[1:])
print(variavel[-5])
print(variavel[0:9])
print(10 * '_')

# len percorre a variavel
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[0:13:3])
print(10 * '_')

# [::-1] inverte a variável
print(variavel[::-1])


