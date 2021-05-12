dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" 

def at_content(my_dna):
    length = len(my_dna) 
    a_count = my_dna.count('A') 
    t_count = my_dna.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content

print("at content is " + str(at_content(dna)))

