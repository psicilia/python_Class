"""
NAME 
    sequence_Info.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>

DESCRIPTION
    modulo de asistencia para el analisis y determinacion de seceuncias de DNA

CATEGORY
    DNA sequence analisis

REQUIERMENTS
    re
USAGE
    from sequence_Info import *
GITHUB
    https://github.com/psicilia/python_Class/blob/1aa83fdc61471c0bd1b430f518ba79ddbad1006b/src/proyecto_final/pkg/sequence_Info_mod1.py

funcions:
    seq_prep(seq):
        modify the secuence to set to uppercase, and remove blanks and -
        returns:    modified string on uppercase and without blanks or - 
    
    seq_valid(seq):
        Determine if the sequence contains valid characters
        raise error if invalid character found
        returns:    boolean, True if sequence is valid

    get_at_content(seq):
        receives a DNA sequence and return AT content
        returns:    float of AT proportion
    
    transcript_data(dna):
        receives a DNA sequence and print important info related to its transcript
        returns:    string of transcript in DNA

    seq_stats(dna):
        receives a DNA sequence and print data related to the number of apearences of A, C, G or T
        prints the results
        returns: none

    protein_base(dna):
        receives a DNA sequence and returns the corresponding protein
        raise error if amount of charecters is not multiple of 3
        returns: string of protein result


"""
import re

class AmbiguousBaseError(Exception):
    '''invalid character found'''
    pass

class MissingCharacters(Exception):
    '''the provided sequence does not contain triplets'''
    pass

#creamos un diccionario con la traduccion de cada triplete
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#funcion que regulariza la secuencia
def seq_prep(seq):
    '''modify the secuence to set to uppercase, and remove blanks and - '''
    # pasamos a mayusculas y removemos espacios y guiones
    new_Seq = seq.upper()
    new_Seq = new_Seq.replace(" ", "")
    new_Seq = new_Seq.replace("-", "")
    return(new_Seq)   

def seq_valid(seq):
    '''Determine if the sequence contains valid characters'''
    try:
        #si encontramos un elemento diferente a A, C, G o T provocamos un error
        if re.search(r"[^ATGC]", seq):
            raise AmbiguousBaseError()
    except AmbiguousBaseError:
        print("sequence can’t be determined, foreign characters found")
        return(False)
    else:
        return(True)

def get_at_content(seq):
    '''receives a DNA sequence and return AT content'''
    #con base en la longitud de la secuencia y la cantidad de As y Ts calculamos el contenido de AT
    length = len(seq)
    a_count = seq.count('A')
    t_count = seq.count('T')
    at_content = (a_count + t_count) / length
    return at_content

def transcript_data(dna):
    '''receives a DNA sequence and print important info related to its transcript, return the DNA transcript'''
    met_ini = 'AUG'
    fin_seq = 'UAA'
    rna = dna.replace('T','U')
    #buscamos el inicio y el final del transcrito e imprimimos sus datos
    inicio = rna.find(met_ini)
    fin = rna.find(fin_seq)
    print('The RNA sequence is: ', rna)
    print('AUG found at: ',inicio)
    print('TAA found at: ',fin)
    print('The transcript is: ',rna[inicio:fin+3])
    #regresamos la cadena del transcrito en forma de DNA
    return(dna[inicio:fin+2])

def seq_stats(dna):
    '''receives a DNA sequence and print data related to the character stadistics'''
    #contamos las apariciones de cada caracter y obtenemos el contenido de AT
    print('A: ', dna.count('A'))
    print('C: ', dna.count('C'))
    print('G: ', dna.count('G'))
    print('T: ', dna.count('T'))
    print('The AT content is: '+ str(get_at_content(dna)))

def protein_base(dna):
    '''receives a DNA sequence and returns the corresponding protein'''
    try:
        dna_script = transcript_data(dna)
        #si la cantidad de caracteres de la cadena no es multiplo de 3 no podemos hacer un analisis adecuado
        if len(dna_script) % 3 != 0:
            raise MissingCharacters()
        codons = []
        protein = []
    except MissingCharacters:
        print("incomplete triplets, missing or extra characters, verify your data")
    else:
        #agregamos los codones encontrados a una lista
        for codon in range(0, len(dna_script), 3):
            codons.append(dna_script[codon : codon + 3])
    
        #agregamos los aminoacidos correspodientes a los codones a una lista
        for codon in codons:
            protein.append(gencode[codon])
        #limpiamos el resultado y regresamos la cadena proteica
        return(str(protein).replace(" ", "").replace("'", "").replace(",", "").replace("[","").replace("]",""))