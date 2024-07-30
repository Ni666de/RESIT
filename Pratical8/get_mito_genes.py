def extract_mitochondrial_genes(fasta_file):
    mito_chromosome = 'Mito'
    mito_genes = []
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                gene_info = line[1:].split()  
                gene_name = gene_info[0].split('.')[0]  
                if gene_info[1] == mito_chromosome:
                    mito_genes.append((gene_name, file.next())) 
    return mito_genes


mito_genes = extract_mitochondrial_genes('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

with open('mito_genes.fa', 'w') as outfile:
    for gene_name, sequence in mito_genes:
        outfile.write(f">{gene_name}\n{sequence}\n")
