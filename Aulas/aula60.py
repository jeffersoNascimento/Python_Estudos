"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
# print('valor' if True else 'Outro valor')
# print('valor' if False else 'Outro valor')

# condicao = 10 == 10
# condicao = 10 != 10
# var = 'Valor' if condicao else 'Outro valor'
# print(var)

# digito = 8
# novo_digito = 0 if digito > 9 else digito
# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)

print('Valor' if True else "Outro valor" if True else 'Fim')
print('Valor' if False else "Outro valor" if False else 'Fim')