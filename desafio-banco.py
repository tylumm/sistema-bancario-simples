menu = """
########## MENU INICIAL ##########

Escolha a opção Desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[f] Finalizar

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = (input(menu))
    
    if opcao == 'd':      
        print("############ DEPÓSITO ############")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else: 
            print("Digite um valor válido!")        
        
    elif opcao == 's':
        print("############# SAQUE! #############")
        valor_saque = float(input("Digite o valor que gostaria de sacar: R$ "))
        
        sem_saldo = valor_saque > saldo
        sem_limite = valor_saque > limite
        sem_saque = numero_saques >= LIMITE_SAQUES
        
        if sem_saldo:
            print("Você não tem saldo suficiente para completar a operação")
        
        elif sem_limite:
            print("Você excedeu o valor máximo de saque, utilize um valor menor")
            
        elif sem_saque:
            print("Você atingiu o numero máximo de saques diários! Tente novamente amanhã")
        
        elif valor_saque <= saldo:
            saldo -= valor_saque          
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
        
        else:
            print("Informe um valor válido!") 
       
        
    elif opcao == 'e':
        print("############# EXTRATO ############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##################################")
        
    elif opcao == 'f':
        print("Atendimento Finalizado com sucesso. Tenha um excelente dia!")
        break
        
    else:
        print("Operação inválida, selecione uma opção válida!")
        
    