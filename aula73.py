""" 
Higher Order Functions 
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, texto):
    return funcao(texto)

v = executa(saudacao, "Good Morning")
print(v)