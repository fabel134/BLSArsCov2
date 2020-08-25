#!/usr/local/bin/env python3.7
#-*- coding: iso-8859-1 -*-

#Import pandas as pd

#with open ("c:/Users/jan/GIT/BLSarscov2/data/demofile.txt", "w") as My_genome

#print(My_genome)

f = open ("c:/Users/jan/GIT/BLSarscov2/data/Sequence.fasta", "r") 
#Recuerda que para los path de python en windows debes poner "C:"
print(f.read())

