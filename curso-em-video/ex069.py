# Exercício Python 069: Crie um programa que leia a idade e o 
# sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

print(f"{'='*6} INICIO DO PROGRAMA {'='*6}")

homens_cadastrados = mulher_menos_20 = total_pessoas_mais_18 = 0

while True:
    print("-"*30)
    print("     CADASTRE UMA PESSOA")
    print("-"*30)

    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()

    if idade > 18:
        total_pessoas_mais_18 += 1
    if sexo == "M":
        homens_cadastrados += 1
    if sexo == "F" and idade < 20:
        mulher_menos_20 += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    
    if continuar == "N":
        break
    
print(f"{'='*6} FIM DO PROGRAMA {'='*6}")

print(f"Total de pessoas com mais de 18 anos: {total_pessoas_mais_18}")
print(f"Ao todo temos {homens_cadastrados} homens cadastrados")
print(f"E temos {mulher_menos_20} mulheres com menos de 20 anos")