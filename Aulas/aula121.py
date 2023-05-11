# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


string = 'Jefferson'
print(string.upper())

palio = Carro('palio')
print(palio.nome)
palio.acelerar()

civic = Carro(nome='Civic')
print(civic.nome)
civic.acelerar()
