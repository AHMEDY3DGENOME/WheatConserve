# 🌾 WheatConserve - Conserved Region & SNP Analysis Tool

WheatConserve is an interactive Streamlit-based application that enables genomic analysis of coding DNA sequences (CDS) from different wheat cultivars. It performs multiple sequence alignment, detects conserved regions and SNPs, generates primers, and allows functional annotation using BLAST.

---

## ✅ Features

- 🔬 Multiple Sequence Alignment using ClustalW
- 🧪 GC Content Analysis across all sequences
- 🟩 Conserved Regions Detection with adjustable threshold
- 🧬 SNP Detection and Filtering by allele variation
- 🧫 Primer Design around filtered SNPs
- 🔗 Functional Annotation via NCBI BLAST (for conserved regions or SNPs)
- 📈 Visual Outputs: GC chart, conserved map, SNP scatter plot
- 📄 Export Options: CSV, Excel, and PDF reports

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-repo/wheatconserve.git
cd wheatconserve
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Ensure ClustalW is installed** and accessible via your system's PATH.

---

## 🚀 Running the App

```bash
streamlit run app.py
```

Then open the link that appears in your terminal.

---

## 📂 Input Requirements

- Upload a multi-sequence FASTA file (.fasta / .fa / .txt) containing CDS sequences of wheat cultivars.

---

## 📤 Output

- GC Content table + chart
- Conserved regions list + plot
- SNPs with allele breakdown
- Primers generated around SNPs
- BLAST-based functional annotation
- Downloadable CSV, Excel, and PDF summaries

---

## 🌐 BLAST Note

BLAST annotation uses the [NCBI BLAST API](https://blast.ncbi.nlm.nih.gov/Blast.cgi) and requires an active internet connection.

---

## 👩‍🔬 For Researchers

This tool is designed for use in:
- Molecular biology
- Wheat genomics
- Genetic diversity studies
- PCR assay design
- Marker-assisted selection

---

## 📝 License

MIT License © 2025 - Developed for research and educational purposes.