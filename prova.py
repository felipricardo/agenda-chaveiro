"""
Faça um único programa na linguagem Python (utilizando o conceito de listas) para controlar a agenda de trabalho de um dia de um chaveiro que realiza atendimento a domicílio. Considere: o sistema deve controlar apenas um dia de trabalho, de um único chaveiro, e ele realiza 12 atendimentos por dia. Armazene toda a agenda
do chaveiro de uma só vez antes do menu do programa, armazenando os seguintes dados em listas separadas mas de igual tamanho: CEP da rua da casa que será atendida, o valor do orçamento do atendimento, e um status para cada agendamento que indica se ele foi ou não realizado (1 REALIZADO, 0 NÃO REALIZADO).
Em seguida apresente um menu com as seguintes opções:
1.Listar atendimentos agendados: caso o usuário selecione essa opção, o programa deverá listar em tela todos os agendamentos mostrando o CEP da casa e o valor do orçamento.
2.Calcular a soma do dinheiro recebido pelo chaveiro: caso o usuário selecione essa opção, o programa deverá passar por todos os atendimento, acumulando o valor do orçamento somente dos
atendimentos que o status foi REALIZADO.
3.Encontrar o CEP do orçamento mais caro e o mais barato: caso o usuário selecione essa opção, o programa deverá passar por todos os atendimentos e encontrar qual foi o atendimento com o orçamento
mais caro e o mais barato (independente do atendimento ter sido ou não realizado) e apresentar o CEP de cada um desses atendimentos.
4. Sair do programa: caso o usuário selecione essa opção, o programa deverá ser encerrado!
"""
# Criação das listas vazias para armazenar os dados dos atendimentos
CEPs = [0] * 12  # lista para armazenar os CEPs dos atendimentos
orcamentos = [0] * 12  # lista para armazenar os valores dos orçamentos dos atendimentos
status = [0] * 12  # lista para armazenar o status dos atendimentos (0 - Não realizado, 1 - Realizado)

# Loop para cadastrar os atendimentos
for a in range(12):
    print("Digite o CEP da casa a ser atendida:")
    CEP = int(input())
    CEPs[a] = CEP

    print("Digite o valor do orçamento:")
    orcamento = float(input())
    orcamentos[a] = orcamento

    print("Digite o status do atendimento (0 - Não realizado, 1 - Realizado):")
    status[a] = int(input())

# Exibe o menu de opções
opcao = 0
while opcao != 4:
    print("\nMenu")
    print("1.	Listar atendimentos agendados")
    print("2.	Calcular a soma do dinheiro recebido pelo chaveiro")
    print("3.	Encontrar o CEP do orçamento mais caro e o mais barato")
    print("4.	Sair do programa")

    print("Digite a opção:")
    opcao = int(input())

    # Opção 1: Listar atendimentos agendados
    if opcao == 1:
        for a in range(12):
            print(f"CEP: {CEPs[a]}, Orçamento: {orcamentos[a]}")

    # Opção 2: Calcular a soma do dinheiro recebido pelo chaveiro
    if opcao == 2:
        total = 0
        for a in range(12):
            if status[a] == 1:
                total += orcamentos[a]
        print(f"A soma do dinheiro recebido pelo chaveiro é: {total}")

    # Opção 3: Encontrar o CEP do orçamento mais caro e o mais barato
    if opcao == 3:
        orcamento_min = orcamentos[0]
        orcamento_max = orcamentos[0]
        CEP_min = CEPs[0]
        CEP_max = CEPs[0]
        for a in range(1, 12):
            if orcamentos[a] < orcamento_min:
                orcamento_min = orcamentos[a]
                CEP_min = CEPs[a]
            if orcamentos[a] > orcamento_max:
                orcamento_max = orcamentos[a]
                CEP_max = CEPs[a]
        print(f"CEP do orçamento mais barato: {CEP_min}, valor: {orcamento_min}")
        print(f"CEP do orçamento mais caro: {CEP_max}, valor: {orcamento_max}")

    # Opção 4: Sair do programa
    if opcao == 4:
        print("Programa encerrado.")
