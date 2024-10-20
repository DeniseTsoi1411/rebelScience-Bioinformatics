from bio_structures import DNA_Codons, Nucleotide_base, RNA_Codons
import random
from collections import Counter

# Notes about classes:
    # Needs a self function ->
    # Private methods ->
class bio_seq:
    """DNA sequence class. Default values: ATCG, DNA, No label"""

    def __init__(self, seq="ATCG", seq_type="DNA", label="No Label"):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence"
        # assert = if sequence is F --> Stop execution of program + send warning

    def validate(self):
        """Function 1 (Validate sequences, Check that it is a valid DNA string)"""
        return set(Nucleotide_base[self.seq_type]).issuperset(self.seq)
    # x.issuperset(y) == Return T if all items from y is present in x
        # i.e., if all of seq is in set Nucleotides, return T

    def get_seq_biotype(self):
        """Returns its sequence type"""
        return self.seq_type

    def get_seq_info(self):
        """Returns 4 strings of the sequence information"""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        """Generates a random sequence of DNA of a specified length"""
        seq = ''.join([random.choice(Nucleotide_base[seq_type])
                       for nuc in range(50)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def nucleotide_frequency(self):
        """Count nucleotide frequency of given string, return as a dictionary"""
        return dict(Counter(self.seq))

    def transcription(self):
        """Check whether it is DNA or RNA.
        DNA -> RNA: replaces Thymine with Uracil
        RNA: Asserts that it is not a valid DNA string"""
        if self.seq_type == "DNA":
            return self.seq.replace("T", "U")  # This makes a copy, does not replace original
        return "Not a DNA sequence"

    def reverse_complement(self):
        """Check whether it is DNA or RNA,
        Reverse complements via mapping on a given string"""
        if self.seq_type == "DNA":
            mapping = str.maketrans("ATCG", "TAGC")
        else:
            mapping = str.maketrans("AUCG", "UAGC")
        return self.seq.translate(mapping)[::-1] # This makes a copy, does not affect original

    def gc_content(self):
        """ Counts the GC contents in a DNA/RNA sequence and output as a percentage"""
        return round((self.seq.count("C") + self.seq.count("G")) / len(self.seq) * 100)

    def gc_content_subsec(self, k=20):
        """ GC content within a subsection (len k) of a sequence. k=20 by default.
        It outputs a list of values with rounded percentage of GC content in each subseq"""
        res = []
        for i in range(0, len(self.seq) - k + 1, k):  # Starts at 0 until the start of the last subseq
            subseq = self.seq[i: i + k]
            res.append(round((subseq.count("C") + subseq.count("G")) / len(subseq) * 100))
        return res

    def translate_seq(self, init_pos=0):
        """Check if sequence is DNA or RNA,
        Extract information from certain amino acid tables depending on type."""
        if self.seq_type == "DNA":
            return [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]
        elif self.seq_type == "RNA":
            return [RNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]

    def codon_usage(self, aminoacid):
        """Checks if sequence is DNA or RNA,
        Shows frequency of a certain aminoacid in a given DNA sequence as proportion.
         i.e., Codon frequency (L): {'CTT': 1.0} means that L has appeared one time due to codon CTT"""
        tmplist = []
        if self.seq_type == "DNA":
            for i in range(0, len(self.seq) - 2, 3):
                if DNA_Codons[self.seq[i:i + 3]] == aminoacid:
                    tmplist.append(self.seq[i:i + 3])

        if self.seq_type == "RNA":
            for i in range(0, len(self.seq) - 2, 3):
                if RNA_Codons[self.seq[i:i + 3]] == aminoacid:
                    tmplist.append(self.seq[i:i + 3])

        freqdict = dict(Counter(tmplist))  # Counter creates a dict
        totalweight = sum(freqdict.values())
        for seq in freqdict:
            freqdict[seq] = round(freqdict[seq] / totalweight, 2)
        return freqdict

    def gen_reading_frames(self):
        """Generates 6 reading frames from a DNA seq, including the reverse complement"""
        frames = []
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        tmpseq = bio_seq(self.reverse_complement(), self.seq_type)
        frames.append(tmpseq.translate_seq(0))
        frames.append(tmpseq.translate_seq(1))
        frames.append(tmpseq.translate_seq(2))
        del tmpseq
        return frames

    def protein_from_rf(self, aa_seq):
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
                if aa == "M":  # Looks for start codon -> Accumulates nucleotides after M
                    current_prot.append("")
                    # To append the first value so can do for loop + makes new entry in case multiple Ms before _s
                for i in range(len(current_prot)):  # For encounters not M or _
                    current_prot[i] += aa
        return proteins

    def all_proteins_from_arfs(self, startreadpos=0, endreadpos=0, ordered=False):
        """First creates all the reading frames from a seq of specified / unspecified range,
        Then, translates the proteins from all reading frames and spot presence/absence of Ms and _s,
        Then orders the list if specified."""
        if endreadpos > startreadpos:  # i.e., have specified the range of reading frame
            tmpseq = bio_seq(self.seq[startreadpos: endreadpos], self.seq_type)
            rfs = tmpseq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()  # if nothing specified, generate rf from whole seq

        res = []
        for rf in rfs:
            prots = self.protein_from_rf(rf)
            for p in prots:
                res.append(p)

        if ordered:  # i.e., if ordered = T
            return sorted(res, key=len, reverse=True)  # key=len == sort by length
        return res