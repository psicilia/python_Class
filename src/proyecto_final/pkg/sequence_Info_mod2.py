"""
NAME 
    sequence_Info_mod2.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>

DESCRIPTION
    modulo de asistencia para lectura, escritura y modificacion de archivos fasta

CATEGORY
    fasta file reading and writing

USAGE
    from pkg.sequence_Info_mod2 import *
GITHUB
    https://github.com/psicilia/python_Class/blob/1aa83fdc61471c0bd1b430f518ba79ddbad1006b/src/proyecto_final/pkg/sequence_Info_mod2.py

funcions:
    write_fasta(sequences, file_name):
        receives a dictionary of sequence name (key) and sequence (key value) and write them in a destination file
        returns:    none 

    add_to_fasta(seq_name, seq, file_name):
        receives a sequence name, a sequence and a destination file and add the sequence in 
        fasta format at the end of the file 
        returns:    none

    read_fasta(file_name):
        receives a fasta file name and read the sequences and saves them on a dictionary
        returns:    dictionary with sequence name as key and sequence as key value 

"""
def write_fasta(sequences, file_name):
    '''receives a dictionary of sequence name (key) and sequence (key value) and write them in a destination file'''
    #abrimos el archivo
    my_Wfile = open(file_name, "W")
    #por cada elemento guardamos en lineas separadas el identificador y la secuencia
    for key in sequences.keys():
        output = ('>'+ str(key) + '\n' + str(sequences[key]) + '\n')
        my_Wfile.write(output)
    #cerramos el archivo 
    my_Wfile.close()


def add_to_fasta(seq_name, seq, file_name):
    '''receives a sequence name, a sequence and a destination file and add the sequence info in fasta format'''
    #abrimos el archivo
    my_Wfile = open(file_name, "a")
    #guardamos en lineas separadas el identificador y la secuencia al final del archivo
    output = ('>'+ str(seq_name) + '\n' + str(seq) + '\n')
    my_Wfile.write(output)
    #cerramos el archivo 
    my_Wfile.close()

def read_fasta(file_name):
    '''receives a fasta file name and read the sequences and returns them on a dictionary'''
    sequences = {}
    #abrimos el archivo
    my_Rfile = open(str(file_name))
    # Leer todas las lineas
    all_lines = my_Rfile.readlines()
    for i in range(0, len(all_lines)):
        if all_lines[i].startswith(">"):
            #por cada linea con el simbolo > agregamos un elemento al diccionario
            #con la linea > como key y la linea siguiente como key value 
            sequences[all_lines[i].replace(">", "").replace("\n","")] = all_lines[i+1].replace("\n","")
    #cerramos el archivo 
    my_Rfile.close()
    #retornamos el diccionario
    return(sequences)


