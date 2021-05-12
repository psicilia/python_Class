"""
NAME 
  tarea4fasta.py

VERSION
  1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>

DESCRIPTION
  generar un archivo fasta con base en las secuencias

CATEGORY
  manejo de archivos

USAGE
  tarea4fasta.py

ARGUMENTS
  none
    
OUTPUT
  output.fasta
    
EXAMPLES
  Example: generamos un archivo fasta con base en la secuencia,
    input: 
      seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG" 
    output: 
      >seq_1
      ATCGTACGATCGATCGATCGCTAGACGTATCG

GITHUB
    [link of the repository]

"""

# Abir archivo
file = open("docs/4-Listas_y_loops/4_dna_sequences.txt")
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

