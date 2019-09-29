# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num1 = randint(0,20)
num2 = randint(0,20)
num3 = randint(0,20)
num4 = randint(0,20)
num5 = randint(0,20)

tupla = (num1,num2,num3,num4,num5)
print("Sua tupla gerada foi: {}".format(tupla))
menor = sorted(tupla)[0]
maior = sorted(tupla)[4]
print("O menor número dessa tupla foi: {}".format(menor))
print("O maior número dessa tupla foi: {}".format(maior))