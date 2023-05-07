# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista in None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Jeff')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernanda', cliente1)
cliente1.append('Eduarda')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente2)

print(cliente1)
print(cliente2)
print(cliente3)