# Sistema bancário interativo com cadastro de usuários

usuarios = []
contas = []
agencia_padrao = "0001"

saldo = 0
extrato_banco = ""
LIMITE_SAQUE = 3
quantidade_saque = 0
usuario_logado = None

menu = '''
[c] Cadastrar usuário
[l] Login
[s] Saque
[d] Depósito
[e] Extrato
[q] Sair
-> 
'''

def criar_usuario():
    cpf = input("CPF (somente números): ")
    if any(u['cpf'] == cpf for u in usuarios):
        print("Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/UF): ")

    usuario = {"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco}
    usuarios.append(usuario)

    numero_conta = len(contas) + 1
    conta = {"agencia": agencia_padrao, "numero": numero_conta, "usuario": usuario}
    contas.append(conta)
    print(f"Usuário {nome} criado com sucesso. Conta: {agencia_padrao}-{numero_conta}")

def login():
    global usuario_logado
    cpf = input("CPF para login: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        usuario_logado = usuario
        print(f"Bem-vindo, {usuario['nome']}!")
    else:
        print("Usuário não encontrado. Cadastre-se primeiro.")

def saque(valor):
    global saldo, extrato_banco, quantidade_saque

    excedeu_saque = saldo < valor
    excedeu_quantidade = quantidade_saque >= LIMITE_SAQUE
    excedeu_limite = valor > 500

    if excedeu_saque:
        return f"Valor de saque inválido, seu saldo é de: R${saldo:.2f}"
    elif excedeu_quantidade:
        return "Excedeu a quantidade de saque diária."
    elif excedeu_limite:
        return "Excedeu o limite de valor por saque (R$500)."
    else:
        saldo -= valor
        quantidade_saque += 1
        extrato_banco += f"Saque: R$ {valor:.2f}\n"
        return f"Saque no valor de R$ {valor:.2f}, realizado com sucesso."

def ver_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_banco else extrato_banco)
    print(f"Saldo: R$ {saldo:.2f}")
    print("========================================")

def deposito(valor):
    global saldo, extrato_banco
    if valor > 0:
        saldo += valor
        extrato_banco += f"Depósito: R$ {valor:.2f}\n"
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."
    else:
        return "Operação falhou! O valor informado é inválido."

while True:
    opcao = input(menu).lower()

    if opcao == 'c':
        criar_usuario()

    elif opcao == 'l':
        login()

    elif opcao == 'd':
        if not usuario_logado:
            print("Faça login para realizar depósitos.")
            continue
        valor = float(input("Informe o valor do depósito: "))
        print(deposito(valor))

    elif opcao == 's':
        if not usuario_logado:
            print("Faça login para realizar saques.")
            continue
        valor = float(input("Informe o valor do saque: "))
        print(saque(valor))

    elif opcao == 'e':
        if not usuario_logado:
            print("Faça login para consultar extrato.")
            continue
        ver_extrato()

    elif opcao == 'q':
        print("Obrigado por utilizar o sistema bancário!")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")
