"""
NAME 
    testingfile.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION


CATEGORY
    test of module 
USAGE
    testingfile.py

GITHUB


"""

from pkg.sequence_Info_mod1 import *
from pkg.sequence_Info_mod2 import *
sequence = "a a g g a t-g t c g c g c-g t t-a t t a g c c t a-a a"

sequence = seq_prep(sequence)

if seq_valid(sequence):
    transcript_data(sequence)
    #print(get_at_content(sequence))
    seq_stats(sequence)
    print(protein_base(sequence))

    print(read_fasta("output.fasta"))