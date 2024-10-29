import textwrap

def cadastrar_usuario(usuarios):
        cpf = input ("Digite seu CPF: ")
        for usuarios in usuarios: 
            if usuarios["cpf"] == cpf:
                print("Este usuário já existe!")
                return
            
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite a data de nascimento: ")
        endereco = input("Digite o endereço (logradouro, numero - bairro - cidade/sigla do estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Usuário cadastrado!")

def cadastrar_conta(AGENCIA, id_conta, usuarios): #vincular com usuário 
        cpf = input("Digite um CPF: ")
        for usuarios in usuarios:
            if usuarios["cpf"] == cpf:
                print("Conta cadastrada!")
                return {"agencia": AGENCIA, "id_conta": id_conta, "usuario": usuarios}
            else:
                print("Usuário não existe!") 
                return          

def listar_contas(contas):
        for conta in contas:
                linha = f"""\
                Agencia: \t{conta['agencia']}
                Numero:\t{conta['id_conta']}
                CPF:\t{conta['usuario']['cpf']}
                """
                print("=" * 100)
                print(textwrap.dedent(linha))
        return
