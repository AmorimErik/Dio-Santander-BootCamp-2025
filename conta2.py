contas_cadastradas = [0]
conta_cliente = {}
cliente = "Erik"

def cadastrar_nova_conta(contas_cadastradas):
    nova_conta = (contas_cadastradas[-1] + 1)
    contas_cadastradas.append(nova_conta)
    return contas_cadastradas

    
    
    
cadastrar_nova_conta(contas_cadastradas)  
    
    
    
print(contas_cadastradas[-1])
