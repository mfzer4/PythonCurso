""" 
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


qualquer_variable = criar_saudacao('Bom dia')
qualquer_variable2 = criar_saudacao('Boa noite')

print(qualquer_variable('Luiz'))
print(qualquer_variable2('Miguel'))

