from Bio.Align import MultipleSeqAlignment
from collections import defaultdict

def find_snps(alignment: MultipleSeqAlignment):
    """
    Detects SNP positions in a given alignment.

    Returns:
    - List of dictionaries with:
        - position (0-based)
        - variation: {base: [seq_ids]}
    """
    snps = []
    aln_len = alignment.get_alignment_length()
    num_seqs = len(alignment)

    for i in range(aln_len):
        column = alignment[:, i]
        unique_bases = set(column.replace("-", ""))

        if len(unique_bases) > 1:
            variation = defaultdict(list)
            for record in alignment:
                base = record.seq[i]
                if base != '-':
                    variation[base].append(record.id)

            snps.append({
                "position": i,
                "variation": dict(variation)
            })

    return snps
