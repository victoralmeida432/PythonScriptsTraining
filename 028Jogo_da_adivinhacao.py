#Exercício Python 028: Escreva um programa que faça o computador 
# "pensar" em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import *

print("Jogo da advinhação, em qual número estou pensando?")
computador = randint(0,5)
jogador = int(input("Digite um número de 0 à 5: "))

if computador == jogador:
    print("Você acertou! eu pensei no número {} ".format(computador))
else:
    print("Você errou, eu pensei no número {}".format(computador))

