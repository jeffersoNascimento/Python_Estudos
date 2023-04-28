# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc ja viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print('---------------------------')

# Avaliação de curto circuito
# print(0 or False or 0.0 or 'abc' or Ture)

senha = input('Senha ') or 'Sem senha'
print(senha)

