#Exercício Python 006: 
# Crie um algoritmo que leia um número e 
# mostre o seu dobro, triplo e raiz quadrada.

numero = float(input("Digite um número para saber seu Dobro,triplo e Raiz quadrada: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print("O dobro de {} é {}. Seu triplo é {} e sua Raíz é {}".format(numero,dobro,triplo,raiz))
