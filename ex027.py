nome_completo = input('Digite seu nome completo: ').strip().lower()
nome_split = nome_completo.split()
primeiro_nome = nome_split[0].capitalize()
tamanho_nome = len(nome_split)-1
ultimo_nome = nome_split[tamanho_nome].capitalize()

print(f"""
Muito prazer em te conhecer!
Seu primeiro nome é {primeiro_nome}
Seu último nome é {ultimo_nome}
    """)