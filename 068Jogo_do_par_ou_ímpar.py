# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

vitorias = 0
par = 0
impar = 0

while True:
    print("Vamos jogar par ou ímpar.")
    computador = randint(1,10)
    user = int(input("Digite um número de 1 à 10: "))
    escolha = str(input("PAR ou ÍMPAR? [P/I]: ")).upper()
    total = user + computador
    if escolha == 'P':
        if total % 2 == 0:
            print("Você venceu...")
            print("Vamos jogar novamente!")
            vitorias += 1
        else:
            print("O computador jogou {}, você jogou {},".format(computador,user))
            print(" o total foi de {} e sua escolha foi {} e por isso você perdeu".format(total,escolha)) 
            break

        if escolha == "I":
            if total % 3 == 0 or total == 1:
                print("Você venceu...")
                print("Vamos jogar novamente!")
                vitorias += 1
            else:
                print("O computador jogou {}, você jogou {},".format(computador,user))
                print(" o total foi de {} e sua escolha foi {} e por isso você perdeu".format(total,escolha)) 
                break

print("FIM")