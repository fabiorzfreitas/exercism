def to_rna(dna_strand):
    rna_strand = []
    for char in dna_strand:
        if char == 'G':
            rna_strand.append('C')
        elif char == 'C':
            rna_strand.append('G')
        elif char == 'A':
            rna_strand.append('U')
        elif char == 'T':
            rna_strand.append('A')
    return ''.join(rna_strand)
