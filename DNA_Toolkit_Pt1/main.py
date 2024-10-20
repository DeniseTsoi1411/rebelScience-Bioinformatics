# # DNA Tool set (Where we will be testing the code)
#
# ## Importing functions from DNAToolkit to test it out
# from DNAToolkit import *        # ("*" = everything)
# import random
# from utilities import coloured
#
# ##### Testing function 1 (With handwritten random string)
# # rndDNAStr = "ATATTATAATATACGeT"  # Random DNA string
# # print(validateSeq(rndDNAStr))
#
# ##### Testing function 1 (With Python generated random string)
# randDNAStr = ''.join([random.choice(Nucleotides)
#                       for nuc in range(50)])
#         # From the 'random' module, it will choose between 20 characters
#             #  from Nucleotide dict and join them tgt with ''
# # print(validateSeq(randDNAStr))
#
# ##### Testing function 2
# # print(countNucFreq(randDNAStr))
#
# ###### Merging both functions together
# DNAStr = validateSeq(randDNAStr)
# # print(countNucFreq(DNAStr))
#
# ##### Testing function 3
# print(f'\nSequence: {coloured(DNAStr)}')
# print(f'1) Sequence Length: {len(DNAStr)}')
# print(coloured(f'2) Nucleotide Frequency: {countNucFreq(DNAStr)}'))
#     # countNucFreq() creates a dictionary, while coloured() requires a str
#         # == Need to pass the while function inside coloured()
# print(f'3) DNA / RNA transcription: {coloured(transcription(DNAStr))}')
# print(f"4) DNA + Reverse Complement:\n     5' {coloured(DNAStr)} 3' ")
#     # Rmb it's in the reversed order
# print(f"        {''.join(['|' for c in range(len(DNAStr))])}")
# print(f"     3' {coloured(reverse_complement(DNAStr)[::-1])} 5'[Complement]")
# print(f"     3' {coloured(reverse_complement(DNAStr))} 5'[Reverse Complement]")
# print(f'5) GC contents: {gc_content(DNAStr)}%')
# print(f'6) GC content in Subsection with k=5 {gc_content_subsec(DNAStr, 5)}')
# print(f'7) Amino acid sequence from DNA: {translate_seq(DNAStr,0)}')
#     # Dont really need the '0', since specified already
# print(f'8) Codon frequency of L: {codon_usage(DNAStr, "L")}')
# print(f'9) Reading frames:')
# for frame in gen_reading_frames(DNAStr):
#     print(frame)
# print(f'10) Proteins in all 6 reading frames:')
# for prot in all_proteins_from_arfs(NM_0002073, 0, 0, True):
#     print(f'{prot}')

from bio_seq import bio_seq
from utilities import read_fasta, readtxtfile, writetxtfile

test_dna = bio_seq()
test_dna.generate_rnd_seq(40, "DNA")
print(test_dna.get_seq_info())

print(test_dna.gc_content_subsec())
print(test_dna.gen_reading_frames())


print(test_dna.all_proteins_from_arfs())

writetxtfile("test.txt", test_dna.seq) # Writes into the test.txt file a sequence of DNA
for rf in test_dna.gen_reading_frames():
    writetxtfile("test.txt", str(rf), 'a')
        # str(rf) == cuz rf is originally a list, want str
        # 'a' == mode == append the lines rather than overwriting. If not, only get the last line

