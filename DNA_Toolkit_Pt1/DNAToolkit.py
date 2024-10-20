# DNA Toolkit file
import collections


########## Part 1: Validating and Counting nucleotides ###########
def validateSeq(dna_seq):
    """Function 1 (Validate sequences, Check that it is a valid DNA string)"""
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


#####   Function 2 (Count frequency of each nucleotide)
# def countNucFreq(seq):
#     tmpFreqDict = {"A":0, "C":0, "G":0, "T":0, }
#     for nuc in seq:
#         tmpFreqDict[nuc] += 1
#     return tmpFreqDict
# Will have an error code if have weird character in seq

def countNucFreq(seq):
    """Function 2 (Counts the frequency of nucleotide occurrences)"""
    return dict(collections.Counter(seq))


# ----------------------------------------------------------------------------------------------------------------------

########## Part 2: Transcription, Reverse Complement ##########
# Aim 1: To be able to create a string that is the reverse complement to original strand
# Aim 2: To transcribe an RNA strand from one DNA strand template

def transcription(seq):
    """Function 3 (Transcription from DNA to RNA strand, replaces Thymine with Uracil)"""
    return seq.replace("T", "U")  # To create an RNA from a DNA strand


# def reverse_complement(seq):
#    """Function 4 (Reverse Complements of forward and backwards strands)"""
#    return ''.join([DNA_reversecomplement[nuc] for nuc in seq])[::-1]
    # Reverse the order + match the bases
    # The brackets confuses mee

def reverse_complement(seq):
    """Function 4.1 (Reverse complements using a faster approach"""
    mapping = str.maketrans("ATCG", "TAGC")
    return seq.translate(mapping)[::-1]
    # maketrans() == Make translations through the mapping
    # Do not require dictionaries for this

# ---------------------------------------------------------------------------------------------------------------------

########## Part 3: GC Content Calculations ##########
# GC-content can be used to denote the genome position of the replication origin
    # CpGs -> Typically found in transcription start sites of genes
# GC content also important for when we design primers + determine efficient PCR conditions
    # High GC = Stronger DNA binding of primer + complementary strand = Higher chance of error
    # Low GC = Favourable (~40%)
        # GC has 3 H-bonds while AT has 2 -> Low GC = Requires lower temperature
#

def gc_content(seq):
    """ Counts the GC contents in a DNA/RNA sequence and output as a percentage"""
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)

def gc_content_subsec(seq, k=20):
    """ GC content within a subsection (len k) of a sequence. k=20 by default.
    It outputs a list of values with rounded percentage of GC content in each subseq"""
    res = []
    for i in range(0, len(seq) - k + 1, k):  # Starts at 0 until the start of the last subseq
        subseq = seq[i : i+k]
        res.append(gc_content(subseq))
    return res

# ---------------------------------------------------------------------------------------------------------------------

########## Part 4: Translation and Codon usage ##########
def translate_seq(seq, init_pos = 0):
    """Translates DNA sequence into amino acid sequence"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq)-2, 3)]
    # Initial position is set to 0 by default (i.e., where to start reading from)
    # Gets the reading frame of 3 and shifts to the next 3 bases

def codon_usage(seq, aminoacid):
    """Shows frequency of a certain aminoacid in a given DNA sequence as proportion.
     i.e., Codon frequency (L): {'CTT': 1.0} means that L has appeared one time due to codon CTT"""
    tmplist = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmplist.append(seq[i:i+3])

    freqdict = dict(collections.Counter(tmplist)) # Counter creates a dict
    totalweight = sum(freqdict.values())
    for seq in freqdict:
        freqdict[seq] = round(freqdict[seq] / totalweight, 2)
    return freqdict

# ---------------------------------------------------------------------------------------------------------------------

########### Part 5: Open Reading Frames ##########
# Ribosomes are proteins that translates mRNA sequence into amino acids
# For every piece of DNA = Can have 6 different reading frames
    # Depends on where it starts (3 options) + Which strand to read (2 options)

def gen_reading_frames(seq):
    """Generates 6 reading frames from a DNA seq, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 2))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 0))
    return frames

# ---------------------------------------------------------------------------------------------------------------------

########## Part 6: Protein search in a reading frame ##########
# Finding proteins in one reading frame within a start and stop codon

def protein_from_rf(aa_seq):
    """Looks for amino acid sequence between a Start and Stop codon and return it to the list 'proteins' """
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":  # Encounters stop codon -> Stop accumulation -> Add current_prot to proteins list
            if current_prot:  # If len(current_prot) > 1:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == "M": # Looks for start codon -> Accumulates nucleotides after M
                current_prot.append("")
                # To append the first value so can do for loop + makes new entry in list in case multiple Ms before _
            for i in range(len(current_prot)):  # For encounters not M or _
                current_prot[i] += aa
    return proteins

# ---------------------------------------------------------------------------------------------------------------------

########## Part 7: Searching for real proteins from NCBI database ##########
# To generate proteins from all reading frames
# Extract the proteins from reading frame
# Return list of proteins sorted or unsorted

def all_proteins_from_arfs(seq, startreadpos=0, endreadpos=0, ordered=False):
    """First creates all the reading frames from a seq of specified / unspecified range,
    Then, translates the proteins from all reading frames and spot presence/absence of Ms and _s,
    Then orders the list if specified."""
    if endreadpos > startreadpos:  # i.e., have specified the range of reading frame
        rfs = gen_reading_frames(seq[startreadpos : endreadpos])
    else:
        rfs = gen_reading_frames(seq)  # if nothing specified, generate rf from whole seq

    res = []
    for rf in rfs:
        prots = protein_from_rf(rf)
        for p in prots:
            res.append(p)

    if ordered:  # i.e., if ordered = T
        return sorted(res, key=len, reverse=True)  # key=len == sort by length
    return res