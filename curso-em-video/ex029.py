velocidade = int(input("Qual é a velocidade atual do carro? "))
multa = (velocidade-80)*7

if velocidade > 80:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print(f"Você deve pagar uma multa de R${multa:.2f}")

print("Tenha um bom dia! Dirija com segurança!")