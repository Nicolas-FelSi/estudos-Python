# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a 
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print("="*30)
print("     10 TERMOS DE UMA PA")
print("="*30)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
ultimo = primeiro + (10-1)*razao

for i in range(primeiro, ultimo+1, razao):   
    print(f"{i} ->", end=" ")
    
print("Acabou")