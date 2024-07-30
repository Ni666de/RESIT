def separate_duplicates(gene_names):
    unique_genes = []
    duplicate_genes = []
    seen = set()

    for gene in gene_names:
        if gene in seen:
            duplicate_genes.append(gene)
        else:
            unique_genes.append(gene)
            seen.add(gene)

    return unique_genes, duplicate_genes


gene_names = ['DLX5', 'DLX6', 'NBAS', 'BRCA2', 'BRCA2', 'NBAS']
unique, duplicates = separate_duplicates(gene_names)
print("Unique genes:", unique)
print("Duplicate genes:", duplicates)
