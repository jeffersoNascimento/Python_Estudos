# Decorator
# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são as funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outrs funções
# Decoradores são "Syntax Sugar" (Açúcar sintática)

def criar_funcao(func): # Função decoradora (decorator)
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print('Ok, você foi decorada')
        return resultado
    return interna

@criar_funcao # Syntax sugar
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('Jefferson')
invertida = inverte_string('456')
print(invertida)
# not_string = inverte_string_checando_parametro(123456)
# print(not_string) # ERROR