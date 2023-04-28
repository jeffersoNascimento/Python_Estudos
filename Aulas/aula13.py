nome = "Jeff Nascimento"
altura = 1.75
peso = 99
imc = peso / altura ** 2

# f-strings (f=formatação)
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos"
linha_3 = f"Seu IMC é {imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
