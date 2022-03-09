conjunto = {1 , 2 , 3 , 4 , 5}

'''Diferencia entre lista y conjunto
conjuntoRepetido = [1,1,2,2,3,5]
lista = [1,1,2,2,3,5]
print(conjuntoRepetido)
print(lista)
'''


print(conjunto)

conjunto.add(20)
print(conjunto)

conjunto.remove(1)
print(conjunto)

conjunto.discard(1)
print(conjunto)

conjunto.pop()  #elimina al azar
print(conjunto)

conjunto.update(1, 2, 3, 4)
print(conjunto)

conjunto.clear()
print(conjunto)