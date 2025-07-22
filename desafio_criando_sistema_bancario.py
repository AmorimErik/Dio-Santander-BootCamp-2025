# Objetivo:
# Iniciar a modelagem do sistema bancário em POO.
# Adicionar classes para cliente e as operações bancárias: depósito e saque.
# Atualizar a implementação dos sistema, para armazenar os dados de clientes e contas bancárias em Objetos, ao invés de dicionários.

# Desafio Extra:
# Atualizar os métodos que tratam as opções do menu, para funcionarem com as classes modeladas.

from abc import ABC, abstractmethod
from datetime import datetime
from zoneinfo import ZoneInfo
import locale, textwrap

try:
    locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "pt_BR")
    except locale.Error:
        print("Locale 'pt_BR' não disponível. Usando o padrão.")

class Cliente:
    # Atributos: endereço e conta.
    def __init__(self, endereco, cidade_uf):
        self.endereco = endereco
        self.cidade_uf = cidade_uf
        self.contas = []
        self.indice_conta = 0
    
    # Metódos: realizar transação e adicionar conta.
    def realizar_registro(self, conta, registro):
        if len(conta.historico.registros_do_dia()) >= 5:
            print(textwrap.indent("Você excedeu o número de transações permitidas para hoje!", "   "))
            return
        
        registro.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class Conta:
    # Atributos privados: (saldo, numero da conta, agencia, cliente, historico)
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._agencia = "0001"
        self._numero_conta = numero_conta
        self._cliente = cliente
        self._historico = Historico()
        
    # Metódos
    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(numero_conta, cliente)
    
    @property
    def saldo(self):
        return self._saldo
      
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(textwrap.indent(f"Valor de R$ {valor:.2f} depositado com sucesso!!!", "   "))
        else:
            print(textwrap.indent("Operação não realizada, valor inválido!", "   "))
            return False
                  
        return True
    
    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print(textwrap.indent("Operação não realizada, saldo insuficiente.", "   "))
            
        elif valor > 0:
            self._saldo -= valor
            print(textwrap.indent("Saque realizado com sucesso!", "   "))
            return True
                
        else:
            print(textwrap.indent("Operação não realizada, valor informado é inválido.", "   "))
    
        return False
    
class Historico:
    # Metódo
    # Adicionar transação(transação: Transação)       
    def __init__(self):
        self._registros = []
    
    @property
    def registros(self):
        return self._registros
    
    def adicionar_transacao(self, registro):
        self._registros.append({
            "tipo": registro.__class__.__name__,
            "valor": registro.valor,
            "data": datetime.now().strftime("%d/%b/%Y - %H:%M:%S")
        })
    
    def gerar_relatorio(self, tipo_registro=None):
        for registro in self._registros:
            if tipo_registro is None or registro["tipo"].lower() == tipo_registro.lower():
                yield registro
    
    def registros_do_dia(self):
        data_atual = datetime.now().date()
        registros_do_dia = []
        for registro in self._registros:
            data_registro = datetime.strptime(registro["data"], "%d/%b/%Y - %H:%M:%S").date()
            if data_atual == data_registro:
                registros_do_dia.append(registro)
        return registros_do_dia
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Conta_Corrente(Conta):
    # Atributos: limite, limite_saques
    def __init__(self, numero_conta, cliente, valor_maximo_saque=500, limite_saque_diario=3):
        super().__init__(numero_conta, cliente)
        self._limite_saque_diario = limite_saque_diario # Limite de saque permitido por dia.
        self._valor_maximo_saque = valor_maximo_saque # Valor máximo permitido por saque.
    
    @property
    def limite_saque_diario(self):
        return self._limite_saque_diario
    
    @property
    def valor_maximo_saque(self):
        return self._valor_maximo_saque
    
    @classmethod
    def nova_conta(cls, cliente, numero_conta, valor_maximo_saque, limite_saque_diario):
        return cls(numero_conta, cliente, valor_maximo_saque, limite_saque_diario)
          
    def sacar(self, valor):
        registros = self.historico.registros
        qtde_saques_hoje = [
            registro for registro in registros
            if registro["tipo"] == Saque.__name__ and datetime.strptime(registro["data"].split(" - ")[0], "%d/%b/%Y").date() == datetime.now().date()
            ]
        
        if valor > self.valor_maximo_saque:
            print(textwrap.indent("Operação não realizada, valor acima do contratado.", "   "))
        elif len(qtde_saques_hoje) >= self.limite_saque_diario:
            print(textwrap.indent("Operaçaõ não realizada, quantidade de saques diários excedido.", "   "))
        else:
            return super().sacar(valor)
            
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero_conta}
            Titular:\t{self.cliente.nome}
            """
            
class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco, cidade_uf):
        super().__init__(endereco, cidade_uf)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def log_registros(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope

@log_registros
def depositar_valor(clientes):
    cpf = input("Informe o CPF do cliente [somente números]: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(textwrap.indent("Cliente não encontrado!", "   "))
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return 
    
    valor_deposito = float(input(textwrap.indent("Informe o valor do depósito: ", "   ")))
    registro = Deposito(valor_deposito)
    
    cliente.realizar_registro(conta, registro)

@log_registros
def sacar_valor(clientes):
    cpf = input("Informe o CPF do cliente [somente números]: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(textwrap.indent("Cliente não encontrado!", "   "))
    
    valor_saque = float(input(textwrap.indent("Informe o valor do saque: ", "   ")))
    registro = Saque(valor_saque)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_registro(conta, registro)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
            
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(textwrap.indent("Cliente encontrato, mas não possui conta cadastrada!", "   "))
        return
    
    return cliente.contas[0]

@log_registros
def exibir_extrato(clientes):
    cpf = input(textwrap.indent("Informe o CPF do cliente [somente números]: ", "   "))
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(textwrap.indent("Cliente não cadastrado.", "   "))
        return
    
    conta = recuperar_conta_cliente(cliente)
    
    if not conta:
        return
    
    print(textwrap.indent("Extrato", "   "))
    registros = conta.historico.registros
    
    extrato = ""
    if not registros:
        extrato = textwrap.indent("Não há movimentação registrada.", "   ")
    
    else:
        for registro in registros:
            extrato += f"\n{registro["data"]}\n{registro['tipo']}\n\tR${registro['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    
def exibir_saldo(clientes):
    cpf = input(textwrap.indent("Informe o CPF do cliente [somente números]: ", "   "))
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(textwrap.indent("Cliente não cadastrado.", "   "))
        return
    
    conta = recuperar_conta_cliente(cliente)
    
    if not conta:
        return
    
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")

@log_registros
def cadastrar_nova_conta(nro_conta, clientes, contas):
    cpf = input(textwrap.indent("Informe o CPF do cliente [somente números]: ", "   "))
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print(textwrap.indent("Cliente não cadastrado.", "   "))
        return
    
    conta = Conta_Corrente.nova_conta(cliente=cliente, numero_conta=nro_conta, valor_maximo_saque=500, limite_saque_diario=3)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print(textwrap.indent("Conta cadastrada com sucesso!", "   "))

@log_registros
def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

@log_registros
def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF do cliente [somente números]: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print(textwrap.indent("Cliente já cadastrado.", "   "))
    else:
        nome = input("Nome completo: ").lower()
        data_nascimento = input("Data de Nascimento no formato [dd/mm/aaaa]: ")
        logradouro = input("Endereço [rua, nº, bairro]: ").lower()
        cidade_uf = input("Cidade/Estado: ").lower()
        cliente = Pessoa_Fisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=logradouro, cidade_uf=cidade_uf)
        clientes.append(cliente)
        print(textwrap.indent("Cliente cadastrado com sucesso!", "   "))

def menu():
    menu = """\n
    ==================== MENU =================== 
    
        Escolha uma opção conforme abaixo:

        [1]\t >>> Depositar
        [2]\t >>> Sacar
        [3]\t >>> Extrato
        [4]\t >>> Saldo
        [5]\t >>> Nova Conta
        [6]\t >>> Novo Cliente
        [7]\t >>> Listar Contas
        [0]\t >>> Sair
        
    =============================================
    """
    return int(input(textwrap.dedent(menu)))

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == 0:
            print(textwrap.dedent("Obrigador por utilizar nosso sistema!!!"))
            break
        elif opcao == 1:
            depositar_valor(clientes)
            
        elif opcao == 2:
            sacar_valor(clientes)
            
        elif opcao == 3:
            exibir_extrato(clientes)
            
        elif opcao == 4:
            exibir_saldo(clientes)
            
        elif opcao == 5:
            nro_conta = len(contas) + 1
            cadastrar_nova_conta(nro_conta, clientes, contas)
            
        elif opcao == 6:
            cadastrar_cliente(clientes)
        
        elif opcao == 7:
            listar_contas(contas)
            
        else:
            print(textwrap.indent("Opção inválida.", "   "))
            
main()