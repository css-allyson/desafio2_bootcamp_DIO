usuario = "Allyson"
saldo = 200.00
saques =[]
depositos =[]
while True:
    acao_usuario = int(input("Digite a opção desejada:\n1 - Sacar\n2 - Depositar\n3 - Consultar o saldo\n4 - Consultar o extrato\n5 - Encerrar\n"))
    if(acao_usuario == 1):
        if(len(saques)>=3):
            print("Seu limite de saques diários foi atingido.")
        else:
            print("Você seleciounou a opção sacar.")
            while True:
                saque = int(input("Digite o valor a ser sacado:"))
                if(saque<0):
                    print("O valor informado para saque não é válido")
                elif(saque>500):
                    print("O limite para saques é de R$500,00 por operação")
                elif(saque>saldo):
                    print("Seu saldo é insuficiente para realizar o saldo no valor informado.")
                else:
                    saldo -=saque
                    saques.append(saque)
                    print("Saque realizado.")
                    break
    elif(acao_usuario ==2):
        print("Você seleciounou a opção depositar.")
        while True:
            deposito = int(input("Digite o valor a ser depositado:"))
            if(deposito<0):
                print("O valor informado para depósito não é válido.")
            else:
                saldo +=deposito
                depositos.append(deposito)
                print("Depósito realizado")
                break        
    elif(acao_usuario ==3):
        print(f"Seu saldo é de R${saldo:.2f}")
    elif(acao_usuario ==4):
        if(len(depositos)>0):
            print("Seus depósitos foram de:")
            for deposito in depositos:
                print(f"R${deposito:.2f}")
        else:
            print("Você não fez depósitos.")
        if(len(saques)>0):
            print("Seus saques foram de:")
            for saque in saques:
                print(f"R${saque:.2f}")
        else:
            print("Você não fez saques.")
    elif(acao_usuario ==5):
        break
    else:
        print("Operação inválida.")
        continue
