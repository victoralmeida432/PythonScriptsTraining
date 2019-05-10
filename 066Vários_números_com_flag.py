# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
cont = 0
flag = True
while flag != False:
    num = int(input("Digite um número [999 p/ Parar]: "))
    if num == 999:
        flag = False
    else:
        cont += 1
        soma += num
print("Foram digitados {} números e a soma entre eles é {}".format(cont,soma))


