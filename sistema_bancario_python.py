#Criando um Sistema Bancário com Python

"""DESCRIÇÃO
Criar um Sistema Bancário em Python.
O objetivo é implementar três operações essenciais: depósito, saque e extrato.
O sistema será desenvolvido para um banco que busca monetizar suas operações.
Criar um sistema funcional que simule as operações bancárias.
"""

#operação de depósito
'''
1 usuário
valores positivos'''

#operação de saque
'''
3 saques diários
limite max 500 por saque
se não tiver limite exibir msg de falta de saldo'''

#operação de extrato
'''
armazenar todas as operações
exibir saldo atual da conta
formato: R$xxx.00'''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Cliente, informe o valor que quer depositar:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, valor inválido.")

    elif opcao == "s":
        valor = float(input("Cliente, informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, não tem esse valor em conta.")
        elif excedeu_limite:
            print("Operação falhou, seu limite é insuficiente")
        elif excedeu_saque:
            print("Operação falhou, o limite diário são 3 saques.")
        
        elif valor > 0:
            saldo == valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou, o valor é inválido")

    elif opcao == "e":
        print("\n+++++++++++Extrato++++++++++\n")
        print("Não houve movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("++++++++++++++++++++++++")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione outra opção.")
