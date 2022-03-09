cadena = 'Estoy utilIzando lOs metodos de Python'
cadena2 = "ESTOY UTILIZANDO LOS METODOS DE PYTHON"

print(cadena2.lower())              #transforma mayus a minus
print(cadena.upper())               #transforma minus a mayus
print(cadena.capitalize())          #primera letra en mayus y el resto minus
print(cadena.title())               #iniciales en mayus
print(cadena.swapcase())            #las mayus a min y las min a mayus
print(cadena[: : 2])                #imprime cada dos espacios
print(cadena[: : -1])               #imprime la cadena en sentido inverso
reemplazar = cadena.replace("" , ",")   #reemplaza el primer caracter dado por el segundo 