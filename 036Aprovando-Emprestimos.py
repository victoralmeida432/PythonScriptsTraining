# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input("Valor da casa: R$: "))
salario = float(input("Salário do comprador R$: "))
anos_financeamento = int(input("Quantos anos de financeamento: "))
prestacao_mensal = valor_da_casa / (anos_financeamento * 12)
salario_percentagem = (salario * 100) / 30

if prestacao_mensal >= salario_percentagem:
    print("Uma casa de R${} com {} anos de financeamento".format(valor_da_casa,anos_financeamento))
    print("Gerará uma parcela de R${} que é maior que 30% do seu salário ({}) e por isso seu emprestimo será negado.".format(prestacao_mensal,salario_percentagem))
else:
    print("Uma casa de R${:.2f} com {} anos de financeamento".format(valor_da_casa,anos_financeamento))
    print("Gerará uma parcela de R${:.2f} que é menor que 30% do seu salário ({:.2f}) e por isso seu emprestimo será aceito.".format(prestacao_mensal,salario_percentagem))