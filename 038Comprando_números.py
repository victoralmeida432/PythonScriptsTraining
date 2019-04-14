#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro número a ser comparado: "))
num2 = int(input("Digite o segundo número a ser comparado: "))

if num1 == 0 and num2 == 0:
    print("Os dois números são iguais a zero,portanto, nenhum é maior que o outro.")
elif num1 > num2:
    print("{} é maior que {}".format(num1,num2))
elif num2 > num1:
    print("{} é maior que {}".format(num2,num1))
elif num1 == num2 or num2 == num1:
    print("{} e {} são iguais".format(num1,num2))