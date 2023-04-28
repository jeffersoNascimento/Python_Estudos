import os

palavra = 'brinquedo'
letra_certa = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        letra_certa += letra

    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra:
        os.system('cls')
        print('VOCÊ GANHOU!!')
        print('Numero de tentativas: ', tentativas)
        letra_certa = ''
        tentativas = 0


    