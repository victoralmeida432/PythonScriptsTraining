# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.

genero = ''
sexo = ''
while genero != "M" and genero != "F":
    genero = str(input("Digite o seu gênero: ")).upper()
    print("O genero escolhido está incorreto.")

    if genero == "M":
        sexo = "Masculino"
    elif genero == "F":
        sexo = "Femenino"
        

print("O seu genero é {}".format(sexo))