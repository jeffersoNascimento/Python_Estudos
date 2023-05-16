# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(name, 'está chamando', self.phone)
        return 4321


call1 = CallMe(': "9876543210"')
retorno = call1('Jefferson Nascimento')
print(retorno)