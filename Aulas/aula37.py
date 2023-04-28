"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

contador = 0

while contador <= 100:
   #continue (gera um loop infinito)
    contador += 1

    if contador == 6: # pula o número 6
        continue

    if contador >=15 and contador <= 35:
        print('##')
        continue

    print(contador)
    
    if contador == 40:
        break
