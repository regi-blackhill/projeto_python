"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# Aspas simples
print('Primeiro teste')
print(1, 'Reggie "Blackhill"', sep='- ', end='\n\n')

# Aspas duplas
print("Segundo teste")
print(2, "Reggie 'Blackhill'", sep='- ', end='\n\n')

# Escape: uma forma poder exibir aspas duplas dentro de uma str com aspas duplas
print("Reggie \"Blackhill\"")

# r usado para expressões regulares, mas permite visualizar o caracter de escape
print(r"Reggie \"Blackhill\"", end='\n\n')

# melhor prática: se quiser exibir aspas duplas, inserir dentro de aspas simples e vice-versa
print('Aspas "duplas" exibidas')
print("Aspas 'simples' exibidas")