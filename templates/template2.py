"""
NAME 
    .py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION


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
     required=True
)
# Execute the parse_args() method
args = parser.parse_args()
