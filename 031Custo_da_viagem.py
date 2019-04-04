# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Digite a distância da viagem: "))
preço_passagem_1 = distancia * 0.50
preço_passagem_2 = distancia * 0.45
if distancia > 200:
    print("O preço total da sua viagem foi: {}".format(preço_passagem_2))
else:
    print("O preço tota da viagem foi: {}".format(preço_passagem_1))