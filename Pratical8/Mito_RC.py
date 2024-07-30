ef reverse_complement_mitochondrial_genes(fasta_file):
    mito_genes = extract_mitochondrial_genes(fasta_file)
    for gene_name, sequence in mito_genes:
        rc_sequence = reverse_complement(sequence.strip())  
        print(f"Gene: {gene_name}, Sequence length: {len(sequence)}, Reverse Complement: {rc_sequence}")
       

filename = input("Enter the filename of the new FASTA file: ")
reverse_complement_mitochondrial_genes(filename)
