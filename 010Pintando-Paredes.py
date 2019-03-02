#Exercício Python 011: 
# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lparede = float(input("Digite a largura da parede: "))
hparede = float(input("Digite a altura da padede: "))
area = (lparede * hparede) / 2
print("Você precisaria de {} Litros de tinta para pintar a sua parede".format(area))