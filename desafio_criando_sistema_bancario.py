
from datetime import datetime
from zoneinfo import ZoneInfo
import locale

locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")

LIMITE_SAQUE_DIARIO = 3 # Limite de saque permitido por dia.
VALOR_MAXIMO_SAQUE = 500.00 # Valor máximo permitido por saque.
extrato = dict()
saldo_consolidado = 0
valor_deposito = 0
valor_saque = 0
saques_realizados = 0 # armazena a quantidade de saques realizada.
opcao = -1
clientes = dict()
contas_cadastradas = [0]
conta_cliente = {}

def cadastrar_cliente(clientes):
    while True:
        cpf = input("CPF (somente números) ou 'sair' para encerrar: ")
        if cpf.lower() == "sair":
            break
        if cpf in clientes:
            print("CPF infomado já cadastrado!")
            cpf = input("Digite um novo CPF ou 'sair' para encerrar: ")
        else:
            nome = input("Nome completo: ").lower()
            data_nascimento = input("Data de Nascimento no formato [dd/mm/aaaa]: ")
            logradouro = input("Endereço [rua, nº, bairro]: ").lower()
            cidade_uf = input("Cidade/Estado: ").lower()
            dados_cliente = {"nome": nome, "data_nascimento": data_nascimento, "logradouro": logradouro, "cidade_uf": cidade_uf}
            clientes[cpf] = dados_cliente
    return clientes


def depositar_valor():
    global saldo_consolidado
    agora = datetime.now()
    data_deposito = agora.strftime("%d/%b/%Y - %H:%M:%S")
    valor_deposito = float(input("""
            =============================================
            Informe o valor do depósito: 
            =============================================
            """))
    if valor_deposito > 0:
        extrato["Depósito", data_deposito] = valor_deposito
        print(f"""
            =============================================
            Valor de R$ {valor_deposito:.2f} depositado com sucesso!!!
            =============================================
        """)
        saldo_consolidado += valor_deposito
    else:
        print("Operação não realizada, valor inválido!")


def sacar_valor(valor_maximo=VALOR_MAXIMO_SAQUE, limite_diario=LIMITE_SAQUE_DIARIO):
    global saldo_consolidado
    global saques_realizados
    agora = datetime.now()
    data_saque = agora.strftime("%d/%b/%Y - %H:%M:%S")
    valor_saque = float(input("""
        ==================================================
                    Informe o valor do saque: 
        ==================================================
        """))
    if valor_saque > saldo_consolidado:
            print("""
        ==================================================
            Operação não realizada, saldo insuficiente.
        ==================================================
            """)
    elif valor_saque > valor_maximo:
            print("""
        ==================================================          
        Operação não realizada, valor acima do contratado.
        ==================================================
        """)
    elif saques_realizados >= limite_diario:
            print("""
        ===============================================
        Operação não realizada, limite diário excedido.
        ===============================================
        """)
    else: 
            saques_realizados += 1
            extrato["Saque", data_saque] = valor_saque
            saldo_consolidado -= valor_saque
            print("""
        =============================================
            Saque realizado com sucesso!!!
        =============================================      
        """)


def exibir_extrato(saldo_consolidado, *,extrato):
    saldo = saldo_consolidado
    agora = datetime.now()
    data_extrato = agora.strftime("%d/%b/%Y - %H:%M:%S")
    if extrato == {}:
        print("Não foram realizadas movimentações!")
    else:
        print(f"""
    ================== EXTRATO =================
    Data:                 {data_extrato}
        """)
        for chave in extrato:
            print(f"{chave}, R$ {extrato[chave]:.2f}")
    print(f"\nSaldo = R$ {saldo:.2f}")


def exibir_saldo():
    global saldo_consolidado
    print(f"""
    =============================================
        Seu saldo é de R$ {saldo_consolidado:.2f}
    =============================================
    """)


def cadastrar_nova_conta(contas_cadastradas, conta_cliente, clientes):
    cpf = input("Para cadastrar uma nova conta, informe o CPF do cliente: ")
    nova_conta = (contas_cadastradas[-1] + 1)
    contas_cadastradas.append(nova_conta)
    conta_cliente[clientes[cpf]["nome"]] = {"Agência": "0001", "Conta": nova_conta}
    return contas_cadastradas, conta_cliente


cadastrar_cliente(clientes)

cadastrar_nova_conta(contas_cadastradas, conta_cliente, clientes)


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
        depositar_valor()

    elif opcao == 2:
        sacar_valor(valor_maximo=VALOR_MAXIMO_SAQUE, limite_diario=LIMITE_SAQUE_DIARIO)
    elif opcao == 3:
        exibir_extrato(saldo_consolidado, extrato=extrato)
    elif opcao == 4:
        exibir_saldo()
    else:
        print("""
        =============================================
            Opção inválida!
        =============================================
        """)
