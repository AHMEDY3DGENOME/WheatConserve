---
title: 'WheatConserve: An Interactive Tool for Conserved Region, SNP Detection, and Primer Design in Wheat CDS Sequences'
authors:
  - name: Ahmed Yassin
    orcid: 0000-0003-2900-7081
    affiliation: 1
affiliations:
  - name: Faculty of Health Sciences, Cape Town University, Computational Biology Department
    index: 1
date: 2025-06-11
bibliography: paper.bib
---

# Summary

WheatConserve is an open-source, interactive bioinformatics tool for identifying conserved coding regions and detecting SNP variations across multiple wheat (*Triticum aestivum*) cultivars using CDS (coding DNA sequence) data. It integrates multiple sequence alignment, SNP filtering, primer design, and functional annotation within an intuitive Streamlit interface.

This tool addresses the practical challenge faced by researchers working on comparative genomics and marker development in wheat, where handling multiple sequence datasets, identifying polymorphic sites, and designing diagnostic primers are often performed via disconnected tools or custom scripts.

WheatConserve provides an integrated solution with visualization capabilities and exportable reports, making it accessible to both computational and wet-lab researchers. The tool also enables the generation of detailed analysis reports in multiple formats (CSV, Excel, PDF), facilitating integration with downstream bioinformatics workflows and documentation. These reports include SNP tables, conserved region summaries, primer lists, and visual figures suitable for publication or laboratory use.

# Statement of Need

Analyzing conserved regions and identifying SNPs in wheat genomes is critical for genetic diversity studies, marker-assisted selection, and breeding programs. Current workflows often rely on using multiple independent tools such as Clustal Omega [@clustalomega2011] for alignment, SNP-sites or custom scripts for SNP extraction, and Primer3 [@primer3_2012] for primer design—each requiring separate handling, file conversions, and parameter tuning.

WheatConserve fills this gap by offering a unified platform for:
- Uploading and aligning CDS sequences
- Detecting conserved regions based on customizable thresholds
- Identifying SNPs from MSA results
- Designing PCR primers around selected polymorphisms
- Annotating gene/protein function via NCBI BLAST
- Visualizing results (GC content, SNP distribution, conserved regions)
- Exporting publication-ready reports in PDF, Excel, and CSV formats for downstream analysis or record-keeping

# Comparison to Existing Tools

While tools like Clustal Omega [@clustalomega2011] and MEGA X [@megax2018] provide excellent support for sequence alignment and basic SNP visualization, they:
- Are not specialized for wheat genomics
- Do not include automated SNP-to-primer workflows
- Lack integration of annotation (e.g., BLAST) and reporting/export features

In contrast, WheatConserve is tailored specifically for wheat CDS data and combines all relevant functionality in a single streamlined environment.

| Feature                      | Clustal Omega | MEGA X | WheatConserve |
|-----------------------------|---------------|--------|----------------|
| CDS-focused workflow        | ❌            | ❌     | ✅             |
| SNP detection from MSA      | ❌            | ✅     | ✅             |
| Automated primer design     | ❌            | ❌     | ✅             |
| Integrated BLAST annotation | ❌            | ❌     | ✅             |
| Streamlit UI (user-friendly)| ❌            | ❌     | ✅             |
| Output in PDF/Excel/CSV     | ❌            | ❌     | ✅             |

# Software Availability

- Source code: https://github.com/AHMEDY3DGENOME/WheatConserve
- License: MIT
- Programming language: Python
- Live demo: https://wheatconserve-mamebvqtw6ckefdcds7rcn.streamlit.app/
- Interface: Streamlit

# Acknowledgements

This project was developed independently as part of a wheat genomics and bioinformatics initiative. Feedback and contributions from the open-source community are appreciated.

# References

WheatConserve compares and builds upon previous tools such as Clustal Omega [@clustalomega2011], MEGA X [@megax2018], Primer3 [@primer3_2012], and Biopython [@cock2009biopython] to deliver a streamlined, integrated workflow for wheat CDS analysis.