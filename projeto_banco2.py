usuarios = [{"nome":"Cleber","data de nascimento":"30/09/1889","cpf":"001.002.003-30","endereço":"Avenida das margaridas Natal, Rio Grande do Norte"}]
contas = [{"agencia":"0001","conta":0,"saldo":100,"saques":[],"depositos":[],"cpf":"001.002.003-30"}]
def validar_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False
def criar_usuario(lista_usuarios,nome, nascimento, cpf, endereco):
    if validar_usuario(lista_usuarios,cpf):
        print("Usuário já cadastrado")
    else:
        usuario = {"nome":nome,"data de nascimento":nascimento,"cpf":cpf,"endereço":endereco}
        lista_usuarios.append(usuario)
        return lista_usuarios
def criar_conta_corrente(lista_contas,lista_usuarios, cpf_usuario):
    if validar_usuario(lista_usuarios,cpf_usuario):
        conta = {"agencia":"0001","conta":len(lista_contas),"saldo":0,"saques":[],"depositos":[],"cpf":cpf_usuario }
        lista_contas.append(conta)
        return lista_contas
    else:
        print("Não há usuário cadastrado para o CPF informado.")
        return lista_contas
def extrato(lista_contas,/,*,conta):
    usuario_existente=False
    for usuario in lista_contas:
        if usuario["conta"]==conta:
            usuario_existente=True
            if(len(usuario["depositos"])>0):
                print("Seus depósitos foram de:")
                for deposito in usuario["depositos"]:
                    print(f"R${deposito:.2f}")
            else:
                print("Você não fez depósitos.")
            if(len(usuario["saques"])>0):
                print("Seus saques foram de:")
                for saque in usuario["saques"]:
                    print(f"R${saque:.2f}")
            else:
                print("Você não fez saques.")
    if usuario_existente == False:
        print("Número de conta não encontrado.")
def deposito(conta,lista_contas,/):
    usuario_existente=False
    for usuario in lista_contas:
        if usuario["conta"]==conta:
            usuario_existente=True
            while True:
                deposito = int(input("Digite o valor a ser depositado:"))
                if(deposito<0):
                    print("O valor informado para depósito não é válido.")
                else:
                    usuario["saldo"] +=deposito
                    usuario["depositos"].append(deposito)
                    print("Depósito realizado")
                    break 
            
    if usuario_existente == False:
        print("Número de conta não encontrado.")
def saque(*,conta,lista_contas):
    usuario_existente=False
    for usuario in lista_contas:
        if usuario["conta"]==conta:
            usuario_existente=True
            if(len(usuario["saques"])>=3):
                print("Seu limite de saques diários foi atingido.")
            else:
                print("Você seleciounou a opção sacar.")
                while True:
                    saque = int(input("Digite o valor a ser sacado:"))
                    if(saque<0):
                        print("O valor informado para saque não é válido")
                    elif(saque>500):
                        print("O limite para saques é de R$500,00 por operação")
                    elif(saque>usuario["saldo"]):
                        print("Seu saldo é insuficiente para realizar o saldo no valor informado.")
                    else:
                        usuario["saldo"] -=saque
                        usuario["saques"].append(saque)
                        print("Saque realizado.")
                        break
            
    if usuario_existente == False:
        print("Número de conta não encontrado.")
def consultar_saldo(conta,lista_contas):
    for usuario in lista_contas:
        if usuario["conta"]==conta:
            usuario_existente=True
            print(f"Seu saldo é de R${usuario["saldo"]:.2f}")
    if usuario_existente == False:
        print("Número de conta não encontrado.") 
def listar_contas(lista_contas):
    for conta in lista_contas:
        print("Número da conta: ")
        print(conta.get('conta'))
        print("CPF do titular da conta: ")
        print(conta.get('cpf'))
        print("\n")
def listar_usuarios(lista_usuarios):
    for usuario in lista_usuarios:
        print("Número da conta: ")
        print(usuario.get('nome'))
        print("\n Endereço: ")
        print(usuario.get('endereço'))
        print("\n Data de nascimento: ")
        print(usuario.get('nascimento'))
        print("\n CPF: ")
        print(usuario.get('cpf'))
        print("\n")
while True:
    acao_usuario = int(input("Digite a opção desejada:\n1 - Sacar\n2 - Depositar\n3 - Consultar o saldo\n4 - Consultar o extrato\n4 - Consultar o extrato\n5 - Cadastrar usuário\n6 - Criar conta\n7 - Listas usuários\n8 - Listar contas\n9 - Encerrar\n"))
    if(acao_usuario == 1):
        #sacar
        print("Você seleciounou a opção saque.")
        conta = int(input("Digite o número da conta para realizar o saque: "))
        saque(conta=conta,lista_contas=contas)

    elif(acao_usuario ==2):
        #Depositar
        print("Você seleciounou a opção depositar.")
        conta = int(input("Digite o número da conta para realizar o depósito: "))
        deposito(conta,contas)      
    elif(acao_usuario ==3):
        #Consultar saldo
        print("Você seleciounou a opção consultar o saldo.")
        conta = int(input("Digite o número da conta para consultar o saldo: "))
        consultar_saldo(conta,contas)
        
    elif(acao_usuario ==4):
        #Consultar extrato
        print("Você seleciounou a opção consultar o extrato.")
        conta = int(input("Digite o número da conta para consultar o extrato: "))
        extrato(contas,conta=conta)

    elif(acao_usuario ==5):
        #Cadastrar usuário
        print("Você seleciounou a opção cadastrar usuário.")
        nome = input("Digite o nome do usuário: ")
        nascimento = input("Digite a data de nascimento: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        usuarios = criar_usuario(usuarios,nome,nascimento,cpf,endereco)

    elif(acao_usuario ==6):
        #Criar conta
        print("Você seleciounou a opção criar conta.")
        cpf = input("Digite o CPF: ")
        contas = criar_conta_corrente(contas,usuarios,cpf)

    elif(acao_usuario ==7):
        #Listar usuários
        print("Você seleciounou a opção listar usuários.")
        listar_usuarios(usuarios)

    elif(acao_usuario ==8):
        #Listar contas
        print("Você seleciounou a opção listar contas.")
        listar_contas(contas)

    elif(acao_usuario ==9):
        break
    else:
        print("Operação inválida.")
        continue
