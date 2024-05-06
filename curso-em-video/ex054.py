# Exercício Python 054: Crie um programa que leia o ano de 
# nascimento de sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date


ano_atual = date.today().year
contador_maior_idade = 0
contador_menor_idade = 0

for i in range(1, 8):
    ano_nasc = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = ano_atual-ano_nasc
    
    if idade >= 21:
        contador_maior_idade += 1
    elif idade > 0 and idade < 21:
        contador_menor_idade += 1
    else:
        print("Ano de nascimento inválido")


print(f"Ao todo tivemos {contador_maior_idade} maiores de idade")
print(f"E também tivemos {contador_menor_idade} menores de idade")