"""
Repetição
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Sru nome é {nome}') # Ctrl+c para interromper o loop infinito

    if nome == 'sair':
        break # interrompe o loop 

print('Acabou')