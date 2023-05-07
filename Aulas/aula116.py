# Criando arquivos com Python
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho = 'F:\\Udemy Curso_python\\Aulas' # Sempre colocar duas barras invertidas no caminho
caminho += 'aula116.txt'

# arquivo = open(caminho, 'w')
# arquivo.close()
with open(caminho, 'w+') as arquivo:
    # print('Olá mundo')
    # print('Arquivo vai ser fechado')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.seek(0, 0)
    print(arquivo.read())

print('#' * 10)

with open(caminho, 'r') as arquivo:
    print(arquivo.read())