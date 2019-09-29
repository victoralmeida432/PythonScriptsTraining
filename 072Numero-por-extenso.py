# Exercício Python 072: 
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

lista = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
        'quinze',"dezesseis","dessete","dezoito","dezenove","vinte")

resultado = None
i = 0

while True:
    núm = int(input("Digite um número de 0 a 20 para saber o seu extenso: "))
    if 0 <= núm <= 20:
        while i < núm:
            print(lista[núm])
            break
        break
    print("Por favor, tente novamente.")
