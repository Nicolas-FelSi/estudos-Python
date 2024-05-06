# Exercício Python 062: Melhore o DESAFIO 061, 
# perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print("Gerador de PA")
print("-="*15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
total = 0
contador = 0
mais_termos = 10

while mais_termos != 0:
    while contador < mais_termos:
        print(f"{termo} -> ", end="")
        termo += razao
        total += 1
        contador += 1
    print("PAUSA")
    
    contador = 0
    
    mais_termos = int(input("Quantos termos você quer mostrar a mais? "))
    
print(f"Progressão finalizada com {total} termos mostrados.")