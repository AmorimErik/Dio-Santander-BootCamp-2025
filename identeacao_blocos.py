def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!", valor)
        print("Retire o seu dinheiro na boca do caixa.")
    else:
        print("Saldo insuficiente!")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(600)