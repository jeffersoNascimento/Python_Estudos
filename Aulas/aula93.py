# try, except, finally e else

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0]) # erro proposital
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome', error.__class__.__name__)
except Exception: # maior classe de erro
    print('ERRO DECONHECIDO.')

print('Continuar')