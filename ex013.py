salario_original = float(input('Qual é o salário do funcionário? R$'))
aumento = 15/100
salario_aumento = salario_original + (salario_original*aumento)

print(f'Um funcionário que ganhava R${salario_original:.2f}, com 15% de aumento,  passa a receber R${salario_aumento:.2f}')