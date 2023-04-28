# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Adivinhe o numero q escolhi de 0 a 10: ')
    letras.add(letra.lower())

    if '5' in letras:
        print(f'Parabéns!')
        break

    print(f'Você digitou: {letras}, ERROU!')