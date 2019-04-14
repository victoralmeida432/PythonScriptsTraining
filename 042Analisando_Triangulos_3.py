# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = float(input("Digite o primeiro seguimento: "))
b = float(input("Digite o segundo seguimento: "))
c = float(input("Digite o terceiro seguimento: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("Seu Triângulo é um EQUILÁTERO.")
    elif a == b or a == c:
        print("Seu Triângulo é um ISÓSCELES.")
    elif a != b and a != c and b != c:
        print("Seu Triângulo é um ESCALENO.")