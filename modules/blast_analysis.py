from Bio.Blast import NCBIWWW, NCBIXML


def run_blast(sequence):
    """
    Runs a BLAST search against the NCBI database.

    Parameters:
    sequence: str - nucleotide sequence to be searched.

    Returns:
    list of BLAST results
    """
    result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
    blast_records = NCBIXML.parse(result_handle)

    results = []
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                results.append({
                    "title": alignment.title,
                    "length": alignment.length,
                    "e_value": hsp.expect,
                    "score": hsp.score,
                    "query_start": hsp.query_start,
                    "query_end": hsp.query_end,
                    "match": hsp.match,
                    "sbjct": hsp.sbjct
                })
    return results