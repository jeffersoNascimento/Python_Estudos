# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Jeff'  # str
# print(string.upper())
# print(isinstance(string, str))
class Person:
    def __init__(self, name, middlename):
        self.name = name
        self.middlename = middlename


p1 = Person('Jefferson', 'Nascimento')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Person('Ana', 'Maria')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.name)
print(p1.middlename)

print(p2.name)
print(p2.middlename)
