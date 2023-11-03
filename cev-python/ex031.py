distancia = float(input('Qual é a distância da sua viagem? '))

if distancia > 200:
    preco_passagem = distancia*0.45
else:
    preco_passagem = distancia*0.50

print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km.')
print(f'E o preço da sua passagem será de R${preco_passagem:.2f}')