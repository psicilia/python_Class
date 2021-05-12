"""
NAME 
  [programName].py

VERSION
  [#.#]

AUTHOR
  Pablo Sicilia Andrade  <[username]@gmail.com>
  [Other authors]: [Modifications]


DESCRIPTION
  [Describe the program]

CATEGORY
  [category of the program: sequence analysis for example]

USAGE
  [programName][-options/arguments]

ARGUMENTS
  [name]  [description]
  [name]  [description]
  [name]  [description]
    
INPUT
  [files or directories used to run the program and formats]
    
OUTPUT
  [file names and formats]
    
EXAMPLES
  [Example 1: describe the example, input and outputs]

GITHUB
    [link of the repository]

"""

# Abir archivo
file = open("dna_sequences.txt")
# Leer todas las lineas y guardarlas en una lista
all_lines = file.readlines()

# Cerrar archivo
file.close()
my_Wfile = open("output.fasta", "w")
# Usar esas lineas en un loop
for line in all_lines:
  print("Length: " + str(len(line)) )
# Usar esas lineas en otro loop
for line in all_lines:
  output = ('>'+ line[:5] + '\n' + line.upper().replace('-','')[9:(len(line)) - 2] + '\n')
  my_Wfile.write(output)
my_Wfile.close()

