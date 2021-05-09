#!/usr/bin/python
archivo_nombre1 = '97-mal.txt'
archivo = open(archivo_nombre1,mode='r')
texto1 = archivo.read()
archivo.close()
# Podemos mostrar en pantalla el archivo que se acaba de cargar
print(texto1)

archivo_nombre2 = '97.txt'
archivo = open(archivo_nombre2,mode='r')
texto2= archivo.read()
archivo.close()
# Podemos mostrar en pantalla el archivo que se acaba de cargar
#print(texto2)


lista1=set([texto1])
lista2=set([texto2])
print(lista1)
final = lista1 & lista2
if len(final) > 0:
	print("hay {} elementos coincidentes".format(len(final)))
	print(final)
else:
	print ("no hay repeticiones")

