"""
Iterando strings com while
"""

nome = input('Digite seu nome: ') # Iteráveis

i = 0
novo_nome = ''
while i < len(nome):
    letra = nome[i]
    i += 1
    novo_nome += f'*{letra}'

print(f'Nome: {novo_nome}*')
    
