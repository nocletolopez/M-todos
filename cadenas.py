#replace
telefono = "+54 261-1234567"
lista_negra = ("+","-"," ")

for x in lista_negra:
    print(telefono)
    telefono = telefono.replace(x,"")

print(telefono)
