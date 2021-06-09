"""
NAME 
    tarea_9_regiones_AT.py

VERSION
    1.0

AUTHOR
    Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    imprimir las regiones ricas en AT si solo hay ATCG 
    en caso contrario imprime los caracteres incorrectos 


CATEGORY

USAGE
  

ARGUMENTS
  -arg    descripcion 

    
INPUT

OUTPUT

GITHUB


"""

import argparse
from os import error, replace

# Create the parser
parser = argparse.ArgumentParser(description="descripcion")
# Argumentos
parser.add_argument("-i", "--input",
    #archivo de entrada, 
    metavar="path/to/file",
    help="direccion del archivo de entrada",
    required=False
    # cambiar en caso de ser necesario 
)
parser.add_argument("-o", "--output", nargs='?', const="not output file" ,
    #archivo de salida, no necesario
    help="Direccion del archivo de salida /n al no definir el output se mostrara en terminal",
     required=False
)
# Execute the parse_args() method
args = parser.parse_args()

import re 

dna = "CGCTC TAGATGCGC ATGACTGCA TGC"
matches = re.finditer(r"[^ATCG]", dna)
for m in matches:
    base = m.group()
    pos = m.start()
    print(base + "found at position " + str(pos))

result = re.split(r"[^ATCG]", dna)
print(result) 
