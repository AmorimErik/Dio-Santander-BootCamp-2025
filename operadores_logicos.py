saldo = 1000
saque = 200
limite = 100
conta_especial = True
contatos_emergencia = []

# Operador E "and"
# AND = pare ser True tudo tem que ser True
print("Operador 'E' (saldo >= saque and saque <= limite) =", saldo >= saque and saque <= limite)

# Operador OU "or"
# OR = para ser True apenas um tem que ser True
print("Operador 'OU' (saldo >= saque or saque <= limite) =", saldo >= saque or saque <= limite)

# Operador de Negação

print("Operador de negação 'not'(not 1000 > 1500) = ", not 1000 > 1500)

print(not contatos_emergencia)

print(not "saque 1500")

print(not "")

# Parênteses
print("Sem parênteses 'saldo >= saque and saque <= limite or conta_especial and saldo >= saque'", saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print("Com parênteses '(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)'", (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))