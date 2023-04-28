"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
vel = input('Velocidade: ') # velocidade atual do carro
velocidade = int(vel)
local_carro = 101 # (kilometro 101) local em que o carro está na estrada

# Constante(variável) deve ser escrita com letra maiúscula

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar está
RADAR_RANGE = 1 # A distância onde o radar pega

passou_velocidade_r1 = velocidade > RADAR_1
passou_pelo_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
multado_radar1 = passou_pelo_radar1 and passou_velocidade_r1

if passou_velocidade_r1 or passou_velocidade_r1 < RADAR_1:
    print(f'Velocidade {velocidade}km carro passou pelo radar')

if passou_velocidade_r1:
    print('Velocidade acima da permitida!')

if multado_radar1:
    print('Carro multado em radar 1')