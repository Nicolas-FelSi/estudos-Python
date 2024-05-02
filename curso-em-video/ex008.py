metros = float(input("Digite um valor(em metros): "))
quilometros = metros/1000
hectametros = metros/100
decametros = metros/10
decimetros = metros*10
centimetros = metros*100
milimetros = metros*1000

print(f"{metros}m é igual a {quilometros:.0f}km")
print(f"{metros}m é igual a {hectametros:.0f}hm")
print(f"{metros}m é igual a {decametros:.0f}dam")
print(f"{metros}m é igual a {decimetros:.0f}dm")
print(f"{metros}m é igual a {centimetros:.0f}cm")
print(f"{metros}m é igual a {milimetros:.0f}mm")