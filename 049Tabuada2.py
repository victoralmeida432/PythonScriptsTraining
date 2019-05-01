# Exercício Python 049: Refaça o DESAFIO 009, 
# mostrando a tabuada de um número que o usuário escolher, 
# só que agora utilizando um laço for.

num = int(input('Digite um número para saber sua tabuada: '))
for c in range(0,11):
    resultado = num * c
    print("{} x {} = {}".format(num,c,resultado))