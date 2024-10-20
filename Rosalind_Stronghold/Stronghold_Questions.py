### Problem 1: Counting DNA nucleotides

# Problem: A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
# the length of a string is the number of symbols that it contains. An example of a length 21 DNA string (whose
# alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
# and 'T' occur in s.

# Example Q + A: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC == 20 12 17 21

def countNucFreq(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0, }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict


DNAStr = "CAGGGTCATTAACATGGTGAGGAGAGTCCGCGACTCTCGCGTGCCTCCACTAGGTTACCTACAACATTAAGTACGAGACTCCCCCAAGACCTTGTCACACGCTC" \
         "ACCTTTGAACTGAGCCTATAAATCATGACGGCTCACACGCGACATCGGAACGCCGTGGGGTCGAATCCGTCCGACCGTCGGGATCAAGGCGAACTACCCGCCAA" \
         "ATATCCAGTCTGCAAGTCTTAGGGGCCGTGAATGAACCTATCTGTGTAAGACCGAATTCGCGCGCAAATCTATCAACTTGATTGCGGTGTGGCTTAGCCTGTAC" \
         "GCCTAATCCCCCCCGCCACGCCTTCACGAACAGCGGCTGCCGCGGGGACTCAGCGCTTATCGACGGACACGCTCGGCGAGGGCTAGTCTAAAGGGTGGGATTAT" \
         "GGTCATGGTTTTCTGGTTCTGATACGCTAGTAAGATCCAAGGGCATCCAAAAGGCTGCAGCATCCTTTTATAATACAAGGGTTTCGGAAAAATACAAGAATTTC" \
         "GTCGAATTGTAGACCCCATTTAAGCTTCAAGGTACGCCGACCGCTATCTCAGTAGCATACAGTGTGAACAAACCTATCGAACAAGTGGGCCGACCAGCTGGTCG" \
         "GACCGAGCAGCGAAGATGGTGCTGAACCAAAGCCATCAATGAGTTCCGAGTGATTAATCATAATTTTGACCATCCACCAAATCCTACACCCAGTCCTCACCAAC" \
         "AGTCGGATACCTGGACGCCTAACCCTCACCTCATACATTTTAGACTCATAACTGAAACAAGGGTCTAGAGATCCAAGATTGTTAGCCCCTGCATACCTTTCCGC" \
         "GGACTGCTCAGCCATTACAGCATGGCTTTTAGCCTGGATAAATCACAATTGCGGCTGCCTATTCCCTCCACCTGCACCCATACTTTCCAGGCGAATAA"
print(' '.join([str(val) for key, val in countNucFreq(DNAStr).items()]))


# ' '.join() = To separate the values by a space
# str(val) = Cuz cant goin integers together (needs to be a string)
# .items() = To provide that it is a set of objects (a pair of items)

# Example solution
def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")
    # Does not need to iterate through the sequence = Faster


# ------------------------------------------------------------------------------------------------------------------------

### Problem 2: Transcribing DNA into RNA

# Problem: An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string t
#  corresponding to a coding strand, its transcribed RNA string u
#  is formed by replacing all occurrences of 'T' in t
#  with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

t = "TTTAGGGGGTTCGACCTTAGTTTCACTAGTCAATATACTGTGCCGCTCCTCTTCCCAGCACATAACGGTACAAGATATATTATGGCACCGGTGCGCACTCTATTGGCTGG" \
    "GAAGATGGTTCGGGCTCCCCGCTAAATGATCGACATGTTACTTGAGGATCCTTAAATGTCCCCAACGCGCGACCCCCTGCATAGGGTTACACCCAATGACAAGTCCGCAC" \
    "TCTTTATAGTCTGGCAGTAACTATGCCGGCTATTTGCTCTTTTCGGTAGTTCCTACTTAGCTGCAGTCAACAGGAAAATAACCTAGCCAGGATCTACAAATGCCCCGGAG" \
    "CATAGATCGAGGCGTTCGGTTAAGTGAGTGCTCGTGTCGTGCGTCTACTAACTGCACGTCCGTGTTCCCAATCAAATAGTCGGGGATATCCCGTTGCTGGCAACGTGCGA" \
    "TAACCCTACACCGTTGCGCCTAGGTCAATCGAAAATCTTTTAAGGTGTGGGCGCCTGTGTATGACTAACTTAGTCAGGCAAGGCCGGGAGGACAATCTCAACTAGGATAG" \
    "CGGCGGTGTCTCGCGTCCAATGCGGCCATCCTGAAGCCCGAGTTTTGACCTCAATCCTACACTCAAGGTGCGTACAGGTATATACCAAGGGCGGCCCCTGAAGAGGCTGA" \
    "TGAGCTCCTGCCCAAGGCAACGCAGGACTTGCTTTTATGATTCCTTGACCGCGCCCGGGGGCTTTCGGAAGAAACTAAACGCGCCAGTTATAAGATGAATGGCGGAGACC" \
    "CGTACAATTCCCATTATAACCTTAATGGATGATTGTCGTACAGATCTGGTTCCCGAGCGATCGCGGTCCTCACTACACCAAGGCTTGGTTCGTAAGTTTTCTAGGTGATT" \
    "ATTCTCATTCTATGGGTTCTGCCCAGGGCCCAATTGTCACGACGC"

# print(t.replace("T", "U"))

# ---------------------------------------------------------------------------------------------------------------------

### Problem 3: Complementing DNA strand

# Problem: In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse
# complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of
# each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s

s = "AACCGTGGAAGCTGATGACTAAGAGTCCTCAACAGGTGTCCGCAGACCATGTAGCACCGAAGAGGAGTGAGCTGCGCCACTTGACAGGATCTCGAGTTCGAACGCCCC" \
    "GTTAGCGAATGAATTTATCTCGCTTAGTCTGACTACACTATGGCAGATACAATACCCGCAAAGTAAGATTGCTAACCAAGGTAACAGTAGACGTCCCTTATTAGCTAA" \
    "TCTCCATAATTATGTTCAATATCGAGGAGGCAGACGATATACGATTGCTGTGCTGTATAGCATGCAAAAGAAGGTGTTAACAGTTGCTTACCAGAATGCAGCTCCGAG" \
    "CGCTAACGAATACGTTAACTCAGGGAGCAAACCCGATAGATTCCCTTTCTATAAATATCATATGTGTATTATGTTGGCGTACACCATACGGGGTAATTTACTCCTTCA" \
    "AAGTTCTCGCTAAATCCCGACATCTAGACGATACCTGGGTCCACTCGAGTCTTAGAATTGAAATATAAGCTTAGAGTGTTACAACACTCTAAGTCGCGAGGTCATGGG" \
    "GGAAGGCAGCCAATAATTGCGTCTCGAGTGTGGCTTTACATCTCTATGAAAACCACCCTAGCTCTGTTCCGTTTGGGCCTCTCTTAACGGCGCAATACTGAAAGTATA" \
    "ACATATCTCCACTCGAACCAAAAGAGCATAGCGGTGATTCAAGGGGGCTCATAATTTAGGTAGCCCCGGTGCTTCTAATGCCAAGCCAGTCAATTTGGAGTCGCGTCA" \
    "TAAACAGTCATACTTATTACACGGCCCTTGGTTAGGGTACCTATGAAATGCGGCGTCACAGGAATGGTTGTTCACTACCCTACAATCGTTCGGACGTGCTTTGGTATA" \
    "CTGCGAGTCAATCCGTCTAGTATTTGTAGAGTGACACCCCAGCACCTTATAGAAGTCAAAGAAATTTCGTT"

print(''.join({"A": "T", "T": "A", "G": "C", "C": "G"}[nuc] for nuc in s)[::-1])


# Somehow doesnt work if dont have the ''.join function
# No need replace function if the nucleotides are defines + have ":" to show replacements
# Curly brackets to reformat the string s
# [nuc] = To index out the nucleotides from the string

# ---------------------------------------------------------------------------------------------------------------------

### Problem 4: Computing GC content

# Problem: The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same
# GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling
# is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
# labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the
# label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx"
# denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note
# on absolute error below.
# Absolute error = |x| +- 0.001

def readfile(filepath):
    """ Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]  # Read line by line and return a list rather than a string
        # Easier to manipulate if it is a list rather than string


def gc_content(seq):
    """ Counts the GC contents in a DNA/RNA sequence and output as a percentage"""
    return round(((seq.count("C") + seq.count("G")) / len(seq) * 100), 6)  # to 6 decimal places


fastafile = readfile("input.txt")
fastadict = {}  # The label becomes the key in the dictionary
fastalabel = ""

for line in fastafile:
    if '>' in line:
        fastalabel = line
        fastadict[fastalabel] = ""
    else:
        fastadict[fastalabel] += line  # Fasta format the string to be in multiple lines

resultdict = {key: gc_content(value) for (key, value) in fastadict.items()}
maxkey = max(resultdict, key=resultdict.get)
print(maxkey)  # Not sure how .get function means to check via values
print(maxkey[1:], resultdict[maxkey])

## Rosalind solution
f = open('input.txt', 'r')

max_gc_name, max_gc_content = '', 0  # max_gc_name == str, max_gc_content == int

buf = f.readline().rstrip()  # This reads line by line == Attaches the first label

# while buf:
#     seq_name, seq = buf[1:], ''  # seq_name = The whole label, seq empty cuz nothing after the label within same line
#     buf = f.readline().rstrip()  # Reads the next line
#     while not buf.startswith('>') and buf:  # Continues if line does not start with '>' + not an empty string!!
#         seq = seq + buf  # Appends the next series of bases to seq
#         buf = f.readline().rstrip()  # Not sure why this line is needed again
#         print('buf', buf)
#     seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
#     if seq_gc_content > max_gc_content:
#         max_gc_name, max_gc_content = seq_name, seq_gc_content # Iterates through the list

print('%s\n%.6f%%' % (max_gc_name, max_gc_content * 100))
f.close()

# ----------------------------------------------------------------------------------------------------------------------

### Problem 5: Fibonacci Numbers

# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# Given: A positive integer of n less than or equals to 25
# Return: The value of Fn

loop = [0, 1,]

def fibonacci_loop(n):
    """Prints the nth fibonacci value"""
    while n+1 > len(loop):
        loop.extend([sum(loop[-2::])])
    print(loop[-1::])

def fibonacci_loop_pythonic(n):
    """A faster way (probably) to find the nth fibonacci value"""
    old, new = 1,1
    for itr in range(n - 1):
        new,old = old, old + new  # new = old, old = old+new
    return new

# ----------------------------------------------------------------------------------------------------------------------
### Problem 6: Rabbits and Recurrence Relations

# Problem: A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences
# can be finite or infinite. Two examples are the finite sequence (π,−√2,0,π) and the infinite sequence of odd numbers
# (1,3,5,7,9,…). We use the notation 'an' to represent the n-th term of a sequence.

# A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms.
# In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive
# the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal
# to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs
# alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence
# relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was
# known to Indian mathematicians over two millennia ago.

# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence
# relation to generate terms for progressively larger values of n. This problem introduces us to the computational
# technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
# generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

def rabbit_loop(n, k):
    """Prints the number of offsprings depending on the number of months (n) and the
    number of offsprings (k), when rabbits follow the fibonacci reproductive cycle.
    o = Small (Children) rabbits -> Requires a month to mature then reproduce
    0 = Mature (Parent) rabbits -> Can reproduce and move to the next cycle

    EG n = 6, k = 2
    Month 1: [o]  # A is child
    Month 2: [0]  # A is adult
    Month 3: [0 o o ]  # A gets 2 kids (a1 a1)
    Month 4: [0 o o 0 0]  # A gets 2 kids (a2 a2) + both a1s matures
    Month 5: [0 o o 0 0 0 o o 0 o o]  # A gets 2 kids (a3 a3) + both a2 matures + a1s both gets 2 kids
    Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]"""
    parent, child = 1,1
    for itr in range(n - 1):
        child, parent = parent, parent + (child * k)
    return child

print(rabbit_loop(30,2))
