#Exercício Python 077: 
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, 
# você deve mostrar, para cada palavra, quais são as suas vogais.


tupla = ('casa','computador','geladeira','televisao','janela','cortina','bolsa','mochila','teclado','mouse','cabo','fone','cesto','roupa')

vogais = []

for item in tupla:
    print("\nNa palavra {} temos:".format(item.upper()),end='')
    for i in item:
        if i in 'a,e,i,o,u':
            print(i,end=' ')




