from random import randint

computador = randint(1,3)
jogador = int(input("""Digite sua opção:
[1] Pedra
[2] Papel
[3] Tesoura 
Sua escolha: """))

if computador == 1:
    if jogador == 1:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Empate.")
    elif jogador == 2:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Vitoria.")        
    elif jogador == 3:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Derrota.")

if computador == 2:
    if jogador == 1:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Derrota.")
    elif jogador == 2:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Empate.")
    elif jogador == 3:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Vitoria.")

if computador == 3:
    if jogador == 1:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Vitoria.")
    elif jogador == 2:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Derrota.")
    elif jogador == 3:
        print("Sua escolha foi: {} e a do computador foi: {}".format(jogador,computador))
        print("Empate.")
