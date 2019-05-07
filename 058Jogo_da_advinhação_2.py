# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai 
# "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print("Digite um número de 1 à 10, se você chutar o mesmo número que pensei, você vence!")
computador = randint(1,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Digite um número: "))
    palpites += 1
    if jogador == computador:
        acertou = True
        print("Você acertou! eu também pensei no número {} ".format(computador))
        print("Foram necessárias {} tentativas".format(palpites))
    else:
        print("Você errou")
