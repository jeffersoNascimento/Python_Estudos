# while/else

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
   #break (se usar o break else não é executado)
else:
    print('O else foi executado.')
print('Fora do while.')
