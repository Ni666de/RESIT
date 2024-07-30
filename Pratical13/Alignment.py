from Bio.SubsMat.MatrixInfo import blosum62
 
def create_complete_blosum62_matrix():
    matrix = {}
    for a in 'ARNDCQEGHILKMFPSTWYV-':
        for b in 'ARNDCQEGHILKMFPSTWYV-':
            matrix[a + b] = blosum62[a + b]
    return matrix
 
blosum62_matrix = create_complete_blosum62_matrix()
 
def calculate_score(seq1, seq2):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += BLOSUM62.get((aa1, aa2), -1) 
    return score

def calculate_identity(seq1, seq2):
    identical = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return (identical / len(seq1)) * 100

def print_alignment_results(seq1, seq2, score, identity_percentage):
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    print(f"Alignment Score: {score}")
    print(f"Identity Percentage: {identity_percentage:.2f}%")

score = calculate_score(seq1, seq2)
identity_percentage = calculate_identity(seq1, seq2)
print_alignment_results(seq1, seq2, score, identity_percentage)
 
