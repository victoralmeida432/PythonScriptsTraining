# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
# Voltar para o Curso

vel_carro = float(input("Digite a velocidade do carro: "))
if vel_carro > 80:
    execesso = vel_carro - 80
    multa = execesso * 7
    print("Você ultrapassou o limite de velocidade, sua multa é de {} reais".format(multa))
else:
    print("Siga com tranquilidade!")