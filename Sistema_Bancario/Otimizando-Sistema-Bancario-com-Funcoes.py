import textwrap

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário 
[c] Criar Conta
[l] Listar Contas
[q] Sair

=> """



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

def saque(*, valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite): #argumento por nome (keyword only)
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        return(saldo, extrato)

def deposito(saldo, valor, extrato , /): #argumentos po posição (positional only)
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        return (saldo, extrato)

def historico(extrato, /, *, saldo ): #argumentos por posição e nome, posicionais: saldo nomeados: extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return

def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    opcao = 0
    LIMITE_SAQUES = 3
    contas = []
    id_conta = 0
    usuarios = []


    while True:

        opcao = input(menu)
        opcao = opcao.lower()
    
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "s":
            saldo, extrato = saque(saldo = saldo , valor = float(input("Informe o valor do saque: ")) , extrato = extrato,limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

        elif opcao == "e":
            historico(extrato, saldo = saldo)

        elif opcao == "u":
            cadastrar_usuario(usuarios)

        elif opcao == "c":
            id_conta = len(contas)+1
            conta = cadastrar_conta(AGENCIA, id_conta, usuarios)

            if conta:
                contas.append(conta) #evitar o bug em caso de retorno vazio, não cadastrar vazios no array

        elif opcao == "l":
             listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    return

main()
