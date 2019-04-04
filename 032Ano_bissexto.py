from datetime import *
ano = int(input("Digite o ano que deseja saber se é bissexto:  // Digite 0 para pegar o ano atual"))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÃO é BISSEXTO".format(ano))