#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input("Digite seu nome completo: "))
nome_separado = nome_completo.split()
print("Seu primeiro nome: {}".format(nome_separado[0]))
print("Seu ultimo nome: {}".format(nome_separado[len(nome_separado)-1]))