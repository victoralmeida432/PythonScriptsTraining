# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        soma = soma + num
        cont = cont + 1
    else:
        break
print("Você digitou {} números e a soma entre eles foi {}.".format(cont,soma))


