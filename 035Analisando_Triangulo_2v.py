# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print("Os Segumentos acima PODEM criar um triângulo.")
else:
    print("Os seguimentos acima NÃO PODEM criar um triângulo.")