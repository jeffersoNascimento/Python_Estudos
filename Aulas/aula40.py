# CALCULADORA COM WHILE
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    num_valido = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    operador_permitido = '+-/*'

    if operador not in operador_permitido:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Resultado abaixo:')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)  


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break

# CALCULADORA COM if

# num1 = input('Digite um número: ')
# num2 = input('Digite outro número: ')

# if num1.isdigit() and num2.isdigit():
#     num1_float = float(num1)
#     num2_float = float(num2)
# else:
#     print('ERROR: Você não digitou número.')

# operacao = input('Digite a operação: ')
    

# if operacao == '+':
#     resultado = num1_float + num2_float

# elif operacao == '-':
#     resultado = num1_float - num2_float

# elif operacao == '*':
#     resultado = num1_float * num2_float

# elif operacao == '/':
#     resultado = num1_float / num2_float
# else:
#     print('Digite uma operação válida')
    

# print(f'{num1_float} {operacao} {num2_float} é igual á: {resultado}')




