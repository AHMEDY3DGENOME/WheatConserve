from Bio.Align import MultipleSeqAlignment

def find_conserved_regions(alignment: MultipleSeqAlignment, threshold: float = 0.9):
    """
    Takes a Biopython MultipleSeqAlignment object and finds conserved regions.

    Parameters:
    - alignment: Biopython alignment object
    - threshold: float between 0 and 1 indicating conservation %

    Returns:
    - List of tuples: (start_index, end_index)
    """
    num_seqs = len(alignment)
    aln_length = alignment.get_alignment_length()

    conserved = []
    current_start = None

    for i in range(aln_length):
        column = alignment[:, i]
        most_common = max(set(column), key=column.count)
        count = column.count(most_common)

        if count / num_seqs >= threshold and most_common != '-':
            if current_start is None:
                current_start = i
        else:
            if current_start is not None:
                conserved.append((current_start, i - 1))
                current_start = None

    if current_start is not None:
        conserved.append((current_start, aln_length - 1))

    return conserved
