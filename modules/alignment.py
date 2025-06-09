from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
import os
import shutil

def run_alignment(input_fasta, output_prefix="aligned"):
    """
    Run ClustalW alignment on a given input FASTA file.
    Returns Biopython alignment object.
    """
    clustalw_path = shutil.which("clustalw2") or shutil.which("clustalw")
    if not clustalw_path:
        raise FileNotFoundError("ClustalW not found. Please install ClustalW and make sure it's in your PATH.")

    output_aln = f"{output_prefix}.aln"

    clustalw_cline = ClustalwCommandline(clustalw_path, infile=input_fasta, outfile=output_aln)
    stdout, stderr = clustalw_cline()

    if not os.path.exists(output_aln):
        raise FileNotFoundError(f"Alignment output file not found: {output_aln}")

    alignment = AlignIO.read(output_aln, "clustal")
    return alignment
