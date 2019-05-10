# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
maior = 0
menor = 0
media = 0
flag = True

while flag != False:
    num = int(input("Digite um número: "))
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input("Você deseja continuar? [S ou N] ")).upper().strip()[0]
    if escolha == 'N':
        flag = False
    else:
        flag = True
media = soma / cont
print("Você digitou {} números e a média foi {}".format(cont,media))
print("O maior valor foi {} e o menor valor foi {}".format(maior,menor))