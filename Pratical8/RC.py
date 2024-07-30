def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(seq))


seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

rc_seq = reverse_complement(seq)
print("The reverse complement sequence is:", rc_seq)
