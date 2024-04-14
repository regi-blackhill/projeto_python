# comentário de 1 linha

"""
DocString
Isso não é um comentário, mas é usado como se fosse.

Permite pular linhas e adicionar notas.
"""

# função print(argumento)
print(12, 34) # por padrão, o separador é o espaço
print(56, 78) # por padrão, adiciona uma quebra de linha.

# sep=' ' adiciona um separador
print(12, 34, sep='-')
print(56, 78, sep=' & ')

# CRLF (Carriage Return Line Feed) \r\n
# versões mais recentes do Windows entende apenas o \n para quebra de linha

# end=' ' adiciona uma instrução no fim do print
# por padrão é end='\r\n'
print(12, 34, sep='-', end='#') # substituiu a quebra de linha por #
print(56, 78, sep='-', end='\n')
print(9, 10, end='\n#\n#')