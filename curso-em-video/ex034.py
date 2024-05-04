salario = float(input("Qual é o salário do funcionário? R$"))

if salario > 1250:
    salario_com_aumento = salario+(salario*(10/100))
else:
    salario_com_aumento = salario+(salario*(15/100))
    
print(f"Quem ganhava R${salario} passa a ganhar R${salario_com_aumento:.2f} agora")