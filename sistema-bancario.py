#Codigo: Desafio DIO 1# Criando um sistema bancario com Python 
menu = """
================MENU=================
|   [1] Deposito                    |
|   [2] Saque                       |
|   [3] Extrato                     |
|   [0] Sair                        |
=====================================
"""

# Variaveis 
saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

#Laço para automatizar o Dialogo (Operações Bancarias)
while True:
    opcao = input(menu)

    #Opção de Deposito
    if opcao == "1": 
        valor = float(input("Informe o valor do deposito: "))

        #Entradda de Valor
        if valor > 0: 
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        #Erro de Entrada
        else: 
            print("Operação falhou! O valor informado é invalido.")
    
    #Opção de Saque
    elif opcao == "2": 
        valor = float(input("Informe o valor do saque: "))

        #Entradda de Valor
        if valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        #Exedeu o Saldo
        elif valor > saldo: 
            print("Operação falhou! Você não tem saldo suficiente.")
        #Exedeu o Limite
        elif valor > limite: 
            print("Operação falhou! O valor execede o limite")
        #Exedeu o Numero de Saques
        elif numero_saques > LIMITE_SAQUES: 
            print("Operação falhou! Numero de saque maximo execedido")
        #Erro de Entrada
        else:
            print("Operação falhou! O valor informado é invalido")
    
    #Opção de Extrato
    elif opcao == "3": 
        print("\n================EXTRATO==============")
        print(extrato if extrato != "" else "Não foram realizados movimentações")
        print(f"\nSaldo: R$ {valor:.2f}")
        print("\n=====================================")
    
    #Opção de Saida (Fim do Laço)*
    elif opcao == "0": 
        break
    
    #Erro de Entrada
    else: 
        print("OPERAÇÃO INVALIDA, porfavor selecione novamente a operação desejada...")
#Fim