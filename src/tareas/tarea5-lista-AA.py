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
    https://github.com/psicilia/python_Class/blob/6f0823757c8489aa67f102d0606406e90c7d3bc7/src/tarea5-lista-AA.py

"""
#definimos la funcion para calcular el porcentaje de un aa en la secuencia
def get_aa_percentage(sequence, aa):
  length = len(sequence)
  aa_count = sequence.count(aa)
  return (100 * aa_count/length)
#ingresamos los datos
seq = input('ingresa la secuencia proteica: ')
temp = input('ingresa los aminiacidos separados por espacios: ')
#transformamos en mayusculas y eliminamos los espacios de la secuencia 
seq = seq.upper().replace(' ', '')
#definimos los aa si el usuario no ingresa ninguno
if temp == '':
      aa_list = 'AILMFWYV'
else:
  aa_list = temp.upper()

#inicializamos el contador de nuetro porcentaje 
cantidad = 0    

#usamos la funcion defininida para cada aa seleccionado
for aa in aa_list:
  cantidad += get_aa_percentage(seq, aa)
#imprimimos el resultado
print(str(cantidad)+ '%' )
