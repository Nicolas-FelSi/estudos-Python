digitado = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(digitado))
print("Só tem espaços? ", digitado.isspace())
print("É um número? ", digitado.isnumeric())
print("É alfabético? ", digitado.isalpha())
print("É alfanumérico? ", digitado.isalnum())
print("Está em maiúsculas? ", digitado.isupper())
print("Está em minúsculas? ", digitado.islower())
print("Está capitalizada? ", digitado.istitle())