# Exercício Python 060: Faça um programa que leia um 
# número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

c = 1
n = int(input("Digite um número para saber seu fatorial: "))
while n != 1:
    c = c*n
    n = n - 1
print(c)
