# O que são?
# A estrutura condicional permite o desvio do fluxo de controle, quando determinadas expressões lógicas são atendidas.

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
else:
    saldo < saque
    print("Saldo insuficiente!")


opcao = int(input("informe uma opção: [1] Sacar \n[2] Extrado: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    print("Opção inválida")