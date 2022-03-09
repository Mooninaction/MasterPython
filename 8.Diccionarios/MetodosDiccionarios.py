diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 6 : 7}

print(diccionario)

diccionario.pop(3)
print(diccionario)

diccionario.get(2) #el valor de la llave "2"
print(diccionario)

diccionario.setdefault(4,5)
print(diccionario)


diccionario.update(diccionario2) #se juntan los diccionarios
print(diccionario)

diccionario.clear()
print(diccionario)

diccionario.copy() 
print(diccionario)