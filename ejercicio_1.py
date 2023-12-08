#Ejercicio difícil
a ="gordon lanzó su curva...&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado…-agrega el comentarista"
print (a)
variable = a.split("&")
#print(variable)

for x in (variable):
    valor = "\n".join(variable)
    for z in valor:
        lista = valor.replace("-","")
        if "..." or "." in lista:
            lista.__add__("\n")
    break
print(lista)

