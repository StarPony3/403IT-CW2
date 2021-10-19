# Program for printing the complement of the DNA strand.ie.reversing it, 
# then swapping the bases for their complement.eg. A for T, and so on

# string
nucleotides = 'GGGTCCTCTTCCTCGTGTCCGTTCTCTAACCTTAGTGCGTATGTCCATGGTGTGGGAATACTCTTTTACGT'


# empty variable for loop to write to
reverse_nucleotides = ""

# 'for' loop for reversing the string and creating a new string of reversed nucleotides
for base in range(len(nucleotides)-1, -1, -1):
    reverse_nucleotides = reverse_nucleotides + nucleotides[base]

 
# nucleotides now need to be changed to their complementary base.
# replacements in lower case, otherwise later substitutions will replace earlier substitutions.
replace_1 = reverse_nucleotides.replace('A', 't')
replace_2 = replace_1.replace('T', 'a')
replace_3 = replace_2.replace('C', 'g')
replace_4 = replace_3.replace('G', 'c')

#convert back to upper case to get final complemented DNA sequence
complemented_DNA = replace_4.upper()

# check code has worked as expected
print ("Original string: ", nucleotides, "\n")
print ("Reversed string: ", reverse_nucleotides, "\n")
print ("Complement string:", complemented_DNA)
