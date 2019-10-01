# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Lápis','1,50','Caderno','5,90','Estojo','3,99','Caneta','5,99')

for item in range(0,len(tupla)):
    if item % 2 == 0:
        print("{}".format(tupla[item]),end =' ')
    else:
        print("R$: {}".format(tupla[item]))

