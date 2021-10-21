# program to mimic DNA transcription and translation, and calculate mass of protein produced


# dictionary of amino acid : mass pairs
mass_dict = {'A' : '71.03711', 'C' : '103.00919', 'D' : '115.02694', 'E' : '129.04259', 'F' : '147.06841', 'G' : '57.02146', 'H' : '137.05891',
             'I' : '113.08406', 'K' : '128.09496', 'L' : '113.08406', 'M' : '131.04049', 'N' : '114.04293', 'P' : '97.05276', 'Q' : '128.05858',
             'R' : '156.10111', 'S' : '87.03203', 'T' : '101.04768', 'V' : '99.06841', 'W' : '186.07931', 'Y' : '163.06333'} 



# dictionary of codon : amino acid pairs
codon_dict = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L', 'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S',
              'UCG' : 'S', 'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : 'Stop', 'UAG' : 'Stop', 'UGU' : 'C', 'UGC' : 'C', 'UGA' : 'Stop', 
              'UGG' : 'W', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V', 'CUA' : 'L', 'AUA' : 'I',
              'GUA' : 'V', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A', 'CCC' : 'P', 'ACC' : 'T',
              'GCC' : 'A', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A', 'CAU' : 'H', 'AAU' : 'N',
              'GAU' : 'D', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'CAG' : 'Q', 'AAG' : 'K',
              'GAG' : 'E', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G', 'CGA' : 'R', 'AGA' : 'R',
              'GGA' : 'G', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G' }


def transcription(DNA):
    '''produces RNA complement to DNA'''
    
    # replaces bases with their complement
    replace_1 = DNA.replace('T', 'a')
    replace_2 = replace_1.replace('A', 'U')
    replace_3 = replace_2.replace('C', 'g')
    replace_4 = replace_3.replace('G', 'c')

    # converts 'replace_4' to uppercase to produce final RNA strand
    RNA = replace_4.upper()

    # prints resulting RNA strand
    print (f"RNA strand: {RNA}\n")

    # passes 'RNA' to next function as argument
    return translation(RNA)



def translation(RNA):
    '''produces correspoding protein to RNA'''
    
    protein = ""

    # reads characters in RNA string in triplets.
    # uses 'codon_dict' to replace each triplet with corresponding amino acid 
    # stops translating if 'stop' codon encountered
    for x in range(0, len(RNA), 3):
        if (RNA[x : x + 3]) in codon_dict:
            if codon_dict.get(RNA[x : x + 3]) == 'Stop':
                break
            else:
                protein = protein + codon_dict.get(RNA[x : x + 3])

    # prints resulting protein
    print (f"Protein: {protein}\n")

    # passes 'protein' to next function as argument
    return protein_mass(protein)


def protein_mass(protein):
    '''calculates mass of protein produced'''

    # uses 'mass_dict to match amino acid with corresponding mass
    # converts dictionary value to 'float' type for addition
    protein_mass = 0
    for x in protein:
        if x in mass_dict:
            protein_mass = protein_mass + float(mass_dict[x])
            
    return (f"Mass of protein: {protein_mass}")


# DNA strand
DNA = 'TAGGAGGCAACCCCATTTCTTGTCGGACTAAGCAGCCCCTTACGCTGATATGTTTCTCGCCTGCCTGGCTCTGAAACATCCACCTCTGGTTGGGTGTGCCACAATGGCTGCAGGCTGATATGCGTAATGGAATGCATAAGACTTAGCCCAAGAGATGGCGCCAAGCTGAGCACAAAGATTTTAACAAATCCACCTGGTCCGCATATTGTCAATGAGGACCGCGATTGATACGCGTAAGAAGATACGGGATAGTCACTTGAGGTTCTCTCCTACGCGAGCAAACGGCCCAGCTATTATGTGAATCCTCGAAGGGGCAGCTGTAACTCGCACCCGATCCCTCAACAAGATGACCACTCCATATTATCACGGCTCCAGTGCTTGTGCTCAAGTCGTGTCTCGCGGGACGATGAGTCACCACCCGGGTGTTCCCCTGCATGAGATTGGAAAGTCCGCTTCTTGAAACGTTTTGACCACCTCCGACCGCTACTAACAAATCGGGTTCGTCATGATCGTCATACACCCCTCTCCTAACTTACAGGCGAGGCACCACACATAAAGCGCCTGATATCTTCAGACCGTGTATTCTTATCACCTGCGTGACGTGATCATCCCCATCAAATACTTCAAGAGAGAGGTTATGACGCCAAGATCGTCGGGGAGACCAATCATAAATGCCCGGCGGAGTGAATATGTGCGTCTTTTGATCGTCGGATCTTTGGCCATATCTATAAAAACCGATTATTTGACGCAGGTCCTACCCAGGATGCTTTCATTCGCGCAAAACATCCATCCCAAAACGGTTTACAACGTTGCCGGTATATTCAAATTGACGGGCGGGTAAGCGAGCCGAGAATAGTTTCGTTTAGTTGCCGTGAAGACGTGCCGTATAAGATGGGGAGAGAGGAGGAGTCTGAGTACAGGCCTAGAGTACAGTTCCTCTCGGCATTACTGAGGCGCGATGTGGATTGGACGGCTGTCCAGCTGATGACACCGA'

# calls first function on 'DNA'
print (transcription(DNA))
