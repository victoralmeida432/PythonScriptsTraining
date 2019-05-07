#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
soma = 0
multiplicar = 0
maior = 0
menor = 0
opcao = 0

while opcao != 5:
    opcao = int(input("""
    O qual operação você deseja fazer?

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

    >>> 
    """))
    if opcao == 1:
        soma = n1 + n2
        print("{} + {} = {}".format(n1,n2,soma))
    elif opcao == 2:
        multiplicar = n1 * n2
        print("{} X {} = {}".format(n1,n2,multiplicar))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            menor = n2
            print("{} é maior que {}".format(maior,menor))
        elif n2 > n1:
            maior = n2
            menor = n1
            print("{} é maior que {}".format(maior,menor))
        else:
            print("Os número são iguais.")
    elif opcao == 4:
        print("Digite os novos números: ")
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    elif opcao == 5:
        opcao = 5
