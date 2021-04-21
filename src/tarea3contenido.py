"""
NAME
  tarea3contenido.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@lcg.unam.mx>
  [Other authors]: [Modifications]


DESCRIPTION
  este porgrama cuenta la cantidad de A, C, G y T

CATEGORY
  category of the program: sequence analysis for example

USAGE
  [programName][-options/arguments]

ARGUMENTS

INPUT
  [files or directories used to run the program and formats]

OUTPUT
  [file names and formats]

EXAMPLES
  secuencia de dna:
    AAGGAUGTCGCGCGTTATTAGCCTAA
  resultado:
    A:  7
    C:  5
    G:  7
    T:  6

GITHUB
    [link of the repository]

"""

dna = 'AAGGAUGTCGCGCGTTATTAGCCTAA'

print('A: ', dna.count('A'))
print('C: ', dna.count('C'))
print('G: ', dna.count('G'))
print('T: ', dna.count('T'))

