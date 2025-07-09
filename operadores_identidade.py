# O que são?
# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na mémoria.

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

# Para comparar se o objeto A ocupa do mesmo campo de memória do objeto B
# is
print(curso is nome_curso)
print(saldo is limite)

# Negação is not
print(saldo is not limite)