import os
print(os.getcwd())
os.chdir("/home/pablo/PycharmProjects/python_Class")
my_file_name = "docs/dna.txt"
my_file = open(my_file_name)
my_file_content = my_file.read()
my_dna = my_file_content.rstrip("\n")

my_Wfile = open("dna.fasta", "w")
my_Wfile.write(">sequence_name \n")
my_Wfile.write(my_dna)