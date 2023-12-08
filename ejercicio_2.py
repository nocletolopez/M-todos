#Ejercicio colecciones
#cadena = input()
#print(cadena)
#cadena = cadena.split()
#print(cadena)
#cadena = set(cadena)
#cadena = list(cadena)
#cadena = cadena.sort(reverse=False)
#print(cadena)

print("Ingresa una oracion")
texto = input()
palabras = texto.split()
#cambia de texto a un conjunto con set
palabras_unicas = set(palabras)
#convierto en una lista para poder ordenar y ordeno 
# con "sorted" en orden alfabetico 
lista = sorted(list(palabras_unicas))
print(lista)
