#!/usr/local/bin/env python3.7
#-*- coding: iso-8859-1 -*-

#Import pandas as pd

#with open ("c:/Users/jan/GIT/BLSarscov2/data/demofile.txt", "w") as My_genome

#print(My_genome)

f = open ("c:/Users/Jose Abel/BetterLab/Git/BLSarscov2/data/gisaid_hcov-19_2020_08_07_19.fasta ", "r") 
#Recuerda que para los path de python en windows debes poner "C:"
#print(f.read())
lineas = f.readlines()
#print(lineas)

for i in lineas:
    #print(i)
    if i == ">" :
        print(i)
    else :
        print(i)
#for i in lineas:
 #   if i = ">":
        #print(m, 'is large')
    #else:
        #print(m, 'is small')

#for i in lineas:
#if i = @^>
#print ("hola")

#Cambiar el nombre del archivo
#linea = f.readlines() #lee el archivo linea por linea
#print(linea)