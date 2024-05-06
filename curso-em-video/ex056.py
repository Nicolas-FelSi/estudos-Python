# Exercício Python 056: Desenvolva um programa que leia o nome, 
# idade e sexo de 4 pessoas. No final do programa, mostre: a média de 
# idade do grupo, qual é o nome do homem mais velho e quantas mulheres 
# têm menos de 20 anos.

media = 0
soma = 0
idade_homem = 0
nome_homem = ""
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"{'-'*5} {i}ª PESSOA {'-'*5}")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    soma += idade
    
    if sexo == "M":
        if i == 1:
            idade_homem = idade
            nome_homem = nome
        elif idade > idade_homem:
            idade_homem = idade
            nome_homem = nome
    elif sexo == "F":
        if idade < 20:
            mulheres_menos_20 += 1
    else:
        print("Sexo inválido")
        
media = soma/4
    
print(f"A média de idade do grupo é de {media:.1f} anos")
print(f"O homem mais velho tem {idade_homem} anos e se chama {nome_homem}")
print(f"Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos")