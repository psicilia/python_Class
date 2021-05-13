"""
NAME 
  tarea5-lista-AA.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
  calcular el porcentaje de un aminoacido en una secuencia dada

CATEGORY
  analisis de secuencia

USAGE
  tarea5-lista-AA.py

ARGUMENTS
  none
    
INPUT
  secuencia de aminoacidos y aminoacidos seleccionados
  (en caso de no seleccionar se buscan aminoacidos hidrofilicos)
    
OUTPUT
  none
    
EXAMPLES
  Example 1: 
    Inputs:
      secuencia: msrslllrfllfllllpplp
      aa: m l
    output: 55.0%

    Example 2: 
    Inputs:
      secuencia: M S R S L L L R F L L F L L L L P P L P
      aa: 
    output:65.0%


GITHUB
    [link of the repository]

"""
def get_aa_percentage(sequence, aa):
  length = len(sequence)
  aa_count = sequence.count(aa)
  return (100 * aa_count/length)

#seq = 'msrslllrfllfllllpplp' 

seq = input('ingresa la secuencia proteica: ')
seq = seq.upper().replace(' ', '')
temp = input('ingresa los aminiacidos separados por espacios: ')
if temp == '':
  aa_list = 'AILMFWYV'
else:
  aa_list = temp.upper()


cantidad = 0    

for aa in aa_list:
  cantidad += get_aa_percentage(seq, aa)

print(str(cantidad)+ '%' )
