dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
total_pagar = (dias_alugado*60) + (km_rodados*0.15)
print(f'O total a pagar é de R${total_pagar:.2f}')