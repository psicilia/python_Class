"""my_file_name = "../docs/dna.txt"
my_file = open(my_file_name)
my_file_content = my_file.read()
my_dna = my_file_content.rstrip("\n")
dna = my_dna
print(dna.count('A'))
print(dna.count('C'))
print(dna.count('G'))
print(dna.count('T'))

AT = (dna.count('A') + dna.count('T')) / (len(dna) )
print("AT = ", AT)

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
monkeys = ["Papiro ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(apes[2])
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
