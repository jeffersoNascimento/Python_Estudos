"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o espaço onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # escopo global

def escopo():
    global x # x =1 (escopo global) pode ser manipulado dentro da função
    x = 10 # escopo local

    def outra_funcao():
        y = 2
        print(x, y)
    
    outra_funcao()

print(x)
escopo()
print(x)