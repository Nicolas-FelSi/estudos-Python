sexo = input('Informe seu sexo: [M/F] ').strip().upper()

while sexo != 'F' and sexo != 'M':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()

print(f'Sexo {sexo} registrado com sucesso')