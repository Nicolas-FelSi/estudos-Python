primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
terceiro_valor = int(input('Terceiro valor: '))
 
if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
     maior_valor = primeiro_valor 
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior_valor = segundo_valor 
else:
    maior_valor = terceiro_valor 
    
if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
     menor_valor = primeiro_valor 
elif segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor_valor = segundo_valor 
else:
    menor_valor = terceiro_valor 
    
print(f'O maior valor é {maior_valor}')
print(f'O menor valor é {menor_valor}')
