# 🌾 WheatConserve – Conserved Regions, SNP & Primer Analysis for Wheat CDS

**WheatConserve** is an interactive bioinformatics tool for analyzing conserved regions and SNP variations across multiple wheat (Triticum aestivum) cultivars using CDS sequences. It also supports automatic primer design and BLAST-based functional annotation.

---

## 🚀 Features

- ✅ Upload multi-sequence FASTA files for wheat cultivars
- ✅ Perform multiple sequence alignment (MSA)
- ✅ Detect **conserved regions** with user-defined threshold
- ✅ Identify and filter **SNPs** (polymorphic positions)
- ✅ Automatically generate **PCR primers** around SNPs
- ✅ Visualize:
  - GC content per sequence
  - SNP distribution
  - Conserved region maps
- ✅ Annotate sequences using **NCBI BLAST**
- ✅ Export results: CSV, Excel, PDF

---

## 🧬 Example Use Case

Upload CDS sequences from different wheat lines. The tool:
- Highlights conserved regions between them
- Finds meaningful polymorphisms
- Designs primers for genetic markers
- Uses BLAST to predict gene/protein functions

Great for wheat genome researchers, molecular biologists, and bioinformatics educators.

---

## 📦 Installation

```bash
git clone https://github.com/AHMEDY3DGENOME/WheatConserve.git
cd wheatconserve
pip install -r requirements.txt
streamlit run app.py
```

---

## 🖼️ Screenshots

Add screenshots in `screenshots/` directory and link them here for better visualization.

---

## 📁 File Structure

```text
├── app.py                  # Main Streamlit application
├── modules/                # Analysis logic
│   ├── alignment.py
│   ├── gc_content.py
│   ├── snp_analysis.py
│   ├── conserved.py
│   └── pdf_report.py
├── requirements.txt        # Python dependencies
├── README.md               # You are here
└── example_data/           # Sample wheat FASTA sequences
```

---

## 🧪 Input Format

Multi-sequence FASTA with unique cultivar IDs:

```fasta
>cultivar_A
ATGC...
>cultivar_B
ATGT...
>cultivar_C
ATGC...
```

---

## 📝 Citation / Acknowledgement

If you use this tool in your research or teaching, please cite:

> Developed by [AHMED YASSIN] as part of a wheat genomics and bioinformatics initiative.

---

## 📬 Feedback / Contributions

Have an idea or issue? Open an issue or pull request.  
Contributions, fixes, and extensions are welcome.

---

## 🌐 Try It Online

> 🔗 [Live Demo on Streamlit Cloud](https://wheatconserve-mamebvqtw6ckefdcds7rcn.streamlit.app/)

---

## 🧠 License

MIT License. Free to use, modify, and distribute.