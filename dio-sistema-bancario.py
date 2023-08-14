from time import sleep 
import os

LIMITE_SAQUES = 3
numero_saques = 0
limite = 500
saldo = 0
deposito = 0
saque = 0
extrato = ""

menu = """
Olá! Seja bem-vindo ao sistema bancário!
Digite a opção desejada:
[1] - Depositar
[2] - Sacar
[3] - Ver extrato
[0] - Sair

=> """
print()

'''
def deposito():
    dep = float(input("Informe o valor do depósito: "))

    if (dep > 0):
        saldo += dep
        extrato += f"Depósito: R$ {dep:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def saque():
    saq = float(input("Informe o valor do saque: "))
    excedeu_saldo = saq > saldo
    excedeu_limite = saq > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo o suficiente!")
    elif excedeu_limite:
        print("Operação falhou! O  valor do saque excede o limite!")
    elif excedeu_saques:
        print("Operação falhou! Limite de saques excedido!")
    elif saq > 0:
        saldo -= saq
        extrato += f"Saque: R$ {saq:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! Valor inválido!")

def extrato():
    print("\n=============== EXTRATO BANCÁRIO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\Saldo: R$ {saldo:.2f}")
    print("==================================================")
'''

while(True):
    opcao = (input(menu))
    
    if opcao == "1":

        os.system("cls")
        dep = float(input("Informe o valor do depósito: "))
        if (dep > 0):
            saldo += dep
            extrato += f"Depósito: R$ {dep:.2f}\n"
            print("Depósito realizado com sucesso!")
            sleep(2)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":

        os.system("cls")
        saq = float(input("Informe o valor do saque: "))
        excedeu_saldo = saq > saldo
        excedeu_limite = saq > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

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
        elif saq > 0:
            saldo -= saq
            extrato += f"Saque: R$ {saq:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            sleep(2)
        else:
            os.system("cls")
            print("Operação falhou! Valor inválido!")
            sleep(2)

    elif opcao == "3":

        os.system("cls")
        print("\n=============== EXTRATO BANCÁRIO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==================================================")
        sleep(2)
    elif opcao == "0":
        break
    else:
        os.system("cls")
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")
        sleep(2)



   
