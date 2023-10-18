nome_completo = input('Digite seu nome completo: ').strip()
maiuscuas = nome_completo.upper()
minusculas = nome_completo.lower()
nome_split = nome_completo.split()
nome_join = ''.join(nome_split)
letras_total = len(nome_join)
primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print(f"""
      Analisando seu nome...
      Seu nome em maiúsculas é {maiuscuas}
      Seu nome em minúsculas é {minusculas}
      Seu nome tem ao todo {letras_total} letras
      Seu primeiro nome é {primeiro_nome} e ele tem {letras_primeiro_nome} letras
      """)
