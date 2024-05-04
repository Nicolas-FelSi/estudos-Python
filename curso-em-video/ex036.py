valor_casa = float(input("Valor da casa: R$"))
salario_comprador = float(input("Salário do comprador: R$"))
anos_financiamento = int(input("Quantos anos de financiamento? "))

prestacao_mensal = valor_casa/(anos_financiamento*12)
minimo = salario_comprador*(30/100)

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos a prestação será de R${prestacao_mensal:.2f}")

if prestacao_mensal > minimo:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")