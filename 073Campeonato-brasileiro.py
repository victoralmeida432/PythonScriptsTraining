# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

tabela = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
     'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
     'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
     'Vasco', 'Sport Recife', 'América-MG', 'Vitória', 'Paraná')

escolha = 0

while escolha != 99:
    print("""Menu:
            1 -> 5 Primeiros Times.
            2 -> Últimos 4 colocados.
            3 -> Times em ordem alfabética.
            4 -> Posicão da Chapecoense
            99 -> Sair do programa. 
            """)
    escolha = int(input("Digite o número ao qual deseja informações: "))
    if escolha < 1 or escolha >= 5:
        print("Por Favor escolha uma opção válida")
    elif escolha == 99:
        print("tenha uma boa noite")
    else:
        if escolha == 1:
            i = 0
            times = []
            for i in range (0,5,1):
                times.append(tabela[i])
            print(times)
        elif escolha == 2:
            print(tabela[16:21])
        elif escolha == 3:
            print(sorted(tabela))
        elif escolha == 4:
            print("A posição da Chape é: {} colocação ".format(tabela.index("Chapecoense")+1))



        
