# Exercício Python 060: Faça um programa que leia um 
# número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# c = 1
# n = int(input("Digite um número para saber seu fatorial: "))
# while n != 1:
#     c = c*n
#     n = n - 1
# print(c)


#from math import factorial
#n = int(input("Digite um número para saber seu fatorial: "))
#f = factorial(n)
#print("O fatorial de {} é {}".format(n,f))


n = int(input("Digite um número para saber seu fatorial: "))
c = n
while c > 0:
  print("{}".format(c),end='')
  print(' x ' if c > 1 else ' = ',end='')
  f *= c
  c -= 1
print("{}".format(f))    