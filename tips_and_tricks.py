########## Trick 1: Hamming distance ##########
# Hamming distance: The number of mismatches between a string of equal length
# EG string 1: "karolin"; string 2: "kathrin"; H-distance == 3 (rol)
# EG string 1: 1011101; string 2: 1001001; H-distance ==  2

dna_str_1 = "TTCGATCCATTG"
dna_str_2 = "ATCAATCGATCG"


## Approach 1: Loops ##
def h_dist_loop(str_1, str_2):
    h_dist = 0
    for position in range(len(str_1)):
        if str_1[position] != str_2[position]:  # Can do this cuz string same length
            h_dist += 1
    return h_dist


## Approach 2: Sets ##
def h_dist_set(str_1, str_2):
    nucleotide_set_1 = set([(x, y) for x, y in enumerate(str_1)])
    nucleotide_set_2 = set([(x, y) for x, y in enumerate(str_2)])
    # for x in range(len(nucleotide_set_1)):
    # print("Sorted list:", sorted(nucleotide_set_1)[x], sorted(nucleotide_set_2)[x])
    # print("Differences:", nucleotide_set_1.difference(nucleotide_set_2))

    return len(nucleotide_set_1.difference(nucleotide_set_2))
    # enumerate() == Creates tuples where it assigns a character an index number, unsorted
    # difference() == Returns a set ({}) of tuples (()) with differences


## Approach 3: Zip ##
def h_dist_zip(str_1, str_2):
    return len([(n1, n2) for n1, n2 in zip(str_1, str_2) if n1 != n2])
    # zip() == Creates a zip object (list of tuples), where 1st tuple has 0th characters of str_1 and str_2
    # Only append mismatch tuples and return its length


## Test ##
print("Loop Hamming Distance:", h_dist_loop(dna_str_1, dna_str_2))  # "end=''" == to print the both lines in one line

print("Set Hamming Distance:", h_dist_set(dna_str_1, dna_str_2))

print("Zip Hamming Distance:", h_dist_zip(dna_str_1, dna_str_2))
