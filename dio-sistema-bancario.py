from time import sleep 
import os
import textwrap

LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_saques = 0
limite = 500
saldo = 0
extrato = ""
usuarios = []
contas = []

menu = """
Olá! Seja bem-vindo ao sistema bancário!
Digite a opção desejada:
[1] - Depositar
[2] - Sacar
[3] - Ver extrato
[4] - Criar usuário
[5] - Criar conta
[6] - Listar contas
[0] - Sair

=> """
print()


def depositar(saldo, valor, extrato,/):

    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        sleep(2)
    else:
         print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        os.system("cls")
        print("Operação falhou! Você não tem saldo o suficiente!")
        sleep(2)
    elif excedeu_limite:
        os.system("cls")
        print("Operação falhou! O  valor do saque excede o limite!")
        sleep(2)
    elif excedeu_saques:
        os.system("cls")
        print("Operação falhou! Limite de saques excedido!")
        sleep(2)
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
        sleep(2)
    else:
        os.system("cls")
        print("Operação falhou! Valor inválido!")
        sleep(2)
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*,extrato):
    print("\n=============== EXTRATO BANCÁRIO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\Saldo: R$ {saldo:.2f}")
    print("==================================================")
    sleep(2)

def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF do usuário (somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        sleep(2)
        return
    nome = str(input("Informe o nome completo do usuário: "))
    data_nascimento = str(input("Informe a data de nascimento do usuário (DD/MM/AAAA): "))
    endereco = str(input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): "))

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
    sleep(2)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        sleep(2)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    sleep(2)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    sleep(2)


while(True):
    opcao = (input(menu))
    
    if opcao == "1":

        os.system("cls")
        saldo, extrato = depositar(saldo, float(input("Informe o valor do depósito: ")),extrato)

    elif opcao == "2":

        os.system("cls")
        saldo, extrato, numero_saques = sacar(saldo=saldo,valor=float(input("Informe o valor do saque: ")),
              extrato=extrato,limite=limite,numero_saques=numero_saques, 
              limite_saques=LIMITE_SAQUES)

    elif opcao == "3":

        os.system("cls")
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":

        os.system("cls")
        criar_usuario(usuarios)
    
    elif opcao == "5":

        os.system("cls")
        num_conta = len(contas)+1
        conta = criar_conta(AGENCIA, num_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == "6":

        os.system("cls")
        listar_contas(contas)

    elif opcao == "0":
        break
    else:
        os.system("cls")
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
        sleep(2)



   
