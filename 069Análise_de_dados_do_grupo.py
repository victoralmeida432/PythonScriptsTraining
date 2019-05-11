# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

maiores_de_idade = homens = mulheres_acima_de_20 = 0 
while True:
    idade = int(input("Digite a idade: "))
    genero = str(input("Digite o genêro [M/F]: ")).strip().upper()[0]
    resp =  ' '
    if idade > 18:
        maiores_de_idade += 1
    if genero == 'M':
        homens += 1
    else:
        if idade > 20:
            mulheres_acima_de_20 += 1
    while resp not in 'SN':
        resp = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break

print("Pessoas acima de 18 anos: {} ".format(maiores_de_idade))
print("Quantidade homens: {}".format(homens))
print("Mulheres acima de 20 anos: {}".format(mulheres_acima_de_20))
