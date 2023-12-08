#insert
lista_1 = [1,2,3,4,5]
n = len(lista_1)# toma com oreferencia el último índice
lista_1.insert(n,30)
print(lista_1)
lista_1.insert(len(lista_1),30)# Hace lo mismo, toma el útltimo índice
print (lista_1)


