#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, 
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
media = 0
homem_mais_velho = ''
mulheres_com_menos_de_vinte = 0
mais_velho = 0
for i in range(1,5):
    print("---- {}ª Pessoa ----".format(i))
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).upper()
    soma_idades += idade
    media = soma_idades / 4

    if sexo == 'M':
        if i == 1:
            homem_mais_velho = nome
            mais_velho = idade
        else:
            if idade > mais_velho:
                homem_mais_velho = nome
                mais_velho = idade
    else:
        if idade < 20:
            mulheres_com_menos_de_vinte += 1
        
print("A média do grupo é: {}".format(media))
print("O nome do homem mais velho é: {}".format(homem_mais_velho))
print("A quantidade de mulheres com menos de 20 anos é: {}".format(mulheres_com_menos_de_vinte))
