#!/usr/local/bin/env python3.7
#-*- coding: iso-8859-1 -*-
#Programa_Nelly.py es un pequeño script lo que hace es concatenar dos columnas, para que al final solo obtegamos una sola. se puede utilizar para cobinar dos celdas deseadas.

import pandas as pd

data = pd.read_csv("c:/Users/Jose Abel/BetterLab/Tesis/abel-lista1", header=None, sep='\t') #importamos a pandas para que pueda leerse nuestro archivo que esta separado por tabulaciones y asi mismo los encabezado no estan definidos.
#print (data)
data1 = data.T #Esta paso nos permite transponer nuestro datos, es decir, las filas se vuelven columnas y viceversa.
#print (data1)
#data3 = data1.iloc[0, 0] +"-"+ data1.iloc[0,1]
#print (data3)
b=range(0,124) #Se tienen que definir un rango para que funcione nuestro for en este caaso un rango de 0-124 que es el tamaño de nuestra muestra.
for i in data1:
    data3 = data1.iloc[b, 0] +"-"+ data1.iloc[b,1] 
    # Este for nos ayuda a "concatenar" dos celdas cuando no tienes un header establecido. El "iloc" tiene la funcion de buscar la posicion de la celda sin necesidad de tener un encabezado. b= filas. 0 y 1 son las columnas que por default python le pone.
data3.to_csv('file2.txt', header=False) # esta ultimo paso nos sirve para guardar en un documento todo los cambios que le hicimos a nuestros datos e igual le tenemos que decir que nos de la informacion sin tomar encabezado por default.

    
    
    




