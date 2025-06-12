# WheatConserve – Conserved Regions, SNP, and Primer Analysis for Wheat CDS

**WheatConserve** is an open-source, interactive bioinformatics tool for identifying conserved coding regions and SNP variations across multiple wheat (*Triticum aestivum*) cultivars using CDS sequences. It also enables automatic primer design and functional annotation via NCBI BLAST.

---

## Key Features

- Upload multi-sequence FASTA files (CDS)
- Perform Multiple Sequence Alignment (MSA)
- Detect conserved regions based on user-defined thresholds
- Identify and filter SNPs (Single Nucleotide Polymorphisms)
- Design PCR primers around selected SNPs
- Visualize:
  - GC content
  - SNP distribution
  - Conserved region maps
- Annotate sequences via NCBI BLAST
- Export results as CSV, Excel, or PDF reports

---

## Example Use Case

Given CDS sequences from multiple wheat cultivars, *WheatConserve*:
- Detects conserved coding regions
- Highlights sequence polymorphisms
- Designs primers suitable for genetic marker development
- Predicts potential gene/protein function using BLAST

This tool is ideal for wheat genomics researchers, plant molecular biologists, and bioinformatics educators.

---

## How It Works

1. Upload a multi-FASTA file with cultivar-specific CDS.
2. The tool performs MSA and analyzes:
   - Conservation scores
   - SNP locations
   - GC content
3. Primer design is triggered for polymorphic regions.
4. Optional BLAST annotation provides functional insights.
5. Export summarized and visualized outputs.

---

## Installation

```bash
git clone https://github.com/AHMEDY3DGENOME/WheatConserve.git
cd WheatConserve
pip install -r requirements.txt
streamlit run app.py
```

---

## Input Format

Multi-sequence FASTA format with unique cultivar identifiers:

```fasta
>cultivar_A
ATGC...
>cultivar_B
ATGT...
>cultivar_C
ATGC...
```

---

## File Structure

```text
├── app.py                  # Main Streamlit interface
├── modules/                # Core analysis modules
│   ├── alignment.py
│   ├── gc_content.py
│   ├── snp_analysis.py
│   ├── conserved.py
│   └── pdf_report.py
├── example_data/           # Example FASTA sequences
├── requirements.txt
└── README.md
```

---

## Screenshots

Screenshots will be added soon. Please check the `screenshots/` directory.

---

## Live Demo

Try WheatConserve on Streamlit Cloud:
https://wheatconserve-mamebvqtw6ckefdcds7rcn.streamlit.app/

---

## License

MIT License – Free to use, modify, and distribute.

---

## Feedback & Contributions

Contributions, bug reports, and suggestions are welcome via GitHub Issues and Pull Requests.

---

## Citation

If you use WheatConserve in your research, please cite:

```bibtex
@misc{wheatconserve2025,
  author       = {Ahmed Yassin},
  title        = {WheatConserve: Conserved Region and SNP Analysis Tool for Wheat CDS},
  year         = {2025},
  howpublished = {\url{https://github.com/AHMEDY3DGENOME/WheatConserve}},
  note         = {Open-source bioinformatics tool},
}
```