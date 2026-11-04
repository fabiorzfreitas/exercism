rna: dict[str: str] = {
    k: v
    for keys, v in [
    (['AUG'], 'Methionine'),
    (['UUU', 'UUC'], 'Phenylalanine'),
    (['UUA', 'UUG'], 'Leucine'),
    (['UCU', 'UCC', 'UCA', 'UCG'], 'Serine'),
    (['UAU', 'UAC'], 'Tyrosine'),
    (['UGU', 'UGC'], 'Cysteine'),
    (['UGG'], 'Tryptophan'),
    (['UAA', 'UAG', 'UGA'], 'STOP')]
    for k in keys
}

def proteins(strand):
    amino_acids: list = []
    for codon in [strand[i:i+3] for i in range(0, len(strand), 3)]:
        if rna.get(codon) == 'STOP':
            break
        else:
            amino_acids.append(rna.get(codon))
    return amino_acids