clientes = dict()

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

cadastrar_cliente(clientes)
print(clientes)
