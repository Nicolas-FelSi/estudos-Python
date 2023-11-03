velocidade = float(input('Qual a velocidade atual? '))

if velocidade > 80:
    multa = (velocidade - 80)*7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')

print('Tenha um bom dia! Dirija com segurança.')