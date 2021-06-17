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


"""
from os import error, replace
from Bio.Seq import Seq


entrada = input("ingrese la secuencia de RNA: ")
rna = Seq(entrada.replace(" ","").upper())
protein = rna.translate(to_stop=True)
print(protein)