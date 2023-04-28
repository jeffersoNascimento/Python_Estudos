frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    letra_apareceu = frase.count(letra_atual)

    if apareceu_mais_vezes < letra_apareceu:
        apareceu_mais_vezes = letra_apareceu
        letra_apareceu_mais = letra_atual


    i += 1
print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais}" ela apareceu: {apareceu_mais_vezes}x')



