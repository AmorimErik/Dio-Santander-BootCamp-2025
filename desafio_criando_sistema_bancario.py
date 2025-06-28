
import time
LIMITE_SAQUE_DIARIO = 3 # Limite de saque permitido por dia.
VALOR_MAXIMO_SAQUE = 500.00 # Valor máximo permitido por saque.
extrato = {}
saldo = 0
valor_deposito = 0
valor_saque = 0
qtd_saques = 0 # armazena a quantidade de saques realizada.
opcao = -1
while opcao != 0:
    opcao = int(input("""
    ==================== MENU ===================
                      
        Escolha uma opção conforme abaixo:

        [1] >>> Depositar
        [2] >>> Sacar
        [3] >>> Extrato
        [4] >>> Saldo
        [0] >>> Sair
    =============================================
    """))
    if opcao == 0:
        print("""
    =============================================
        Obrigador por utilizar nosso sistema!!!
    =============================================
    """)
        break
    elif opcao == 1:
        valor_deposito = float(input("""
        =============================================
        Informe o valor do depósito: 
        =============================================
        """))
        if valor_deposito > 0:
            extrato["Depósito", time.ctime()] = valor_deposito
            print(f"""
            =============================================
            Valor de {valor_deposito} depositado com sucesso!!!
            =============================================
            """)
            saldo += valor_deposito
        else:
            print("Operação não realizada, valor inválido!")
    elif opcao == 2:
        valor_saque = float(input("""
        =============================================
            Informe o valor do saque: 
        =============================================
        """))
        if qtd_saques > LIMITE_SAQUE_DIARIO:
            print("""
        =============================================
            Saque não autorizado, 
            limite de saque diário excedido.
        =============================================
            """)
        elif valor_saque > VALOR_MAXIMO_SAQUE:
            print("""
        =============================================          
            Saque não realizado, 
            valor acima do permitido.
        =============================================
        """)
        elif valor_saque > saldo:
            print("""
        =============================================
            Saque não autorizado, saldo insuficiente.
        =============================================
        """)
        else: 
            qtd_saques += 1
            extrato["Saque", time.ctime()] = valor_saque*(-1)
            print("""
        =============================================
            Saque realizado com sucesso!!!
        =============================================      
        """)
        saldo -= valor_saque
    elif opcao == 3:
        if extrato == {}:
            print("Não foram realizadas movimentações!")
        else:
            print("""
    ================== EXTRATO =================
            """)
            for chave in extrato:
                print(chave, extrato[chave])
            print(f"Saldo = R$ {saldo:.2f}")
    elif opcao == 4:
        print(f"""
        =============================================
        Seu saldo é de R$ {saldo:.2f}
        =============================================
        """)
    else:
        print("""
        =============================================
              Opção inválida!
        =============================================
        """)