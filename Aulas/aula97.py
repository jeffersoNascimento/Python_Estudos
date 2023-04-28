# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Voçê pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__ está e as pastas
# abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O Python conhece todos os módulos e pacotes presentes
# nos caminhos sys.path
# import sys
# sys.path.append('/home')
import aula97_m
from aula97_m import soma, variavel_modulo

# print('Este módulo se chama:', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(1, 2))
print(aula97_m.soma(4, 5))
# print(*sys.path, sep='\n')



# PROJETO QUE VI NO INSTAGRAM
# import turtle

# x = 0
# y = 0

# turtle.bgcolor('black')
# turtle.speed(0)
# turtle.pencolor('green')
# turtle.penup()
# turtle.goto(0, 100)
# turtle.pendown()

# while True:
#     turtle.forward(x)
#     turtle.right(y)
#     x += 1
#     y += 1
#     if y == 200:
#         break

# turtle.exitonclick()
