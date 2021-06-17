"""
NAME 
    tarea_10_rosalind.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que traduce una secuencia de RNA a proteina

CATEGORY
    sequence translation

USAGE
    tarea_10:_rosalind.py 

ARGUMENTS
    no arguments needed

    
INPUT
    AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

OUTPUT
    MAMAPRTEINSTRING
GITHUB
    https://github.com/psicilia/python_Class/blob/bd4d89751d193b1175eb4e5a8e3535a12837fd41/src/tareas/tarea_10_rosalind.py

"""
from os import error, replace
from Bio.Seq import Seq


entrada = input("ingrese la secuencia de RNA: ")
#Guardamos la secuencia, para poder eliminar espacios y trasformar a mayusculas 
rna = Seq(entrada.replace(" ","").upper())
#transformamos a secuencia y guardamos en rna 
protein = rna.translate(to_stop=True)
#imprimimos el resultado de la traduccion
print(protein)