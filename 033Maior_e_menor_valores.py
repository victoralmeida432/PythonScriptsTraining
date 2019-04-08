#Exercício Python 033: Faça um programa que leia três números e 
# mostre qual é o maior e qual é o menor.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O número {} é maior que {} e {}".format(num1,num2,num3))
elif num2 > num1 and num2 > num3:
    print("O número {} é maior que {} e {}".format(num2,num1,num3))
else:
    print("O número {} é maior que {} e {}".format(num3,num1,num2)