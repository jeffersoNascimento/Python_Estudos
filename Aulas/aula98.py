import importlib

import aula98_m

print(aula98_m.multiplica(2, 5))

for i in range(5):
    # import aula98_m # singleton: só pode existir uma instancia
    importlib.reload(aula98_m)
    print(i)