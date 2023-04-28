# FORMATAÇÃO DE STRINGS COM O MÉTODO FORMAT
a = "A"
b = "B"
c = 1.1

#formato = "a={} b={} c={}".format(a, b, c)

#string = "a={2} b={1} c={0}"
#formato = string.format(a, b, c)

string = "a={nome1} b={nome2} c={nome3:.2f}"
formato = string.format(nome1= a, nome2= b, nome3= c)

print(formato)