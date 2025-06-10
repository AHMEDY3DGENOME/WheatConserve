import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import tempfile
from io import BytesIO
from Bio.Seq import Seq
import requests
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align import AlignInfo
from modules import gc_content, conserved, snp_analysis, pdf_report, blast_analysis
from Bio import SeqIO

def run_alignment(filepath):
    records = list(SeqIO.parse(filepath, "fasta"))
    max_len = max(len(record.seq) for record in records)
    for record in records:
        record.seq = record.seq + Seq("-") * (max_len - len(record.seq))
    return MultipleSeqAlignment(records)

def plot_conserved_regions(alignment_length, conserved_regions):
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, alignment_length)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("Alignment Position")
    ax.set_title("Conserved Regions Map")
    ax.hlines(0.5, 0, alignment_length, colors="lightgray", linestyles="dashed")

    for start, end in conserved_regions:
        width = end - start + 1
        rect = Rectangle((start, 0.25), width, 0.5, color="green", alpha=0.6)
        ax.add_patch(rect)
        ax.text(start + width / 2, 0.8, f"{start}-{end}", ha="center", fontsize=8)

    plt.tight_layout()
    return fig

st.set_page_config(layout="wide")
st.title("🌾 WheatConserve - Conserved Region & SNP Analysis")

st.markdown("""
Upload multiple CDS sequences (FASTA format) from different wheat cultivars.  
This tool performs multiple sequence alignment, highlights conserved regions, detects SNPs, and allows functional annotation.
""")

uploaded_file = st.file_uploader("Upload a FASTA file with multiple sequences", type=["fasta", "fa", "txt"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".fasta") as tmp_fasta:
        tmp_fasta.write(uploaded_file.read())
        tmp_fasta_path = tmp_fasta.name

    try:
        st.success("✅ File uploaded successfully. Running alignment...")

        alignment_result = run_alignment(tmp_fasta_path)

        st.subheader("🧪 GC Content Analysis")
        gc_results = gc_content.calculate_gc_content(alignment_result)
        df_gc = pd.DataFrame(gc_results)
        st.dataframe(df_gc)

        avg_gc = df_gc["gc_content"].mean()
        st.write(f"📊 **Average GC% across all sequences:** {round(avg_gc, 2)}%")

        st.subheader("📈 GC% Distribution")
        fig_gc, ax_gc = plt.subplots(figsize=(8, 3))
        ax_gc.bar(df_gc["id"], df_gc["gc_content"], color="mediumblue")
        ax_gc.set_ylabel("GC%")
        ax_gc.set_title("GC Content per Sequence")
        ax_gc.set_xticklabels(df_gc["id"], rotation=45, ha="right", fontsize=8)
        st.pyplot(fig_gc)

        st.subheader("📈 Alignment Summary")
        st.text(f"Number of sequences: {len(alignment_result)}")
        st.text(f"Alignment length: {alignment_result.get_alignment_length()}")

        st.subheader("💌 Aligned Sequences (First 300 bases)")
        for record in alignment_result:
            st.text(f">{record.id}\n{record.seq[:300]}...")

        snps = snp_analysis.find_snps(alignment_result)

        st.subheader("👥 Conserved Regions")
        threshold = st.slider("Select conservation threshold", 0.5, 1.0, 0.9, 0.05)
        conserved_regions = conserved.find_conserved_regions(alignment_result, threshold)

        if conserved_regions:
            df_conserved = pd.DataFrame(conserved_regions, columns=["Start", "End"])
            st.dataframe(df_conserved)
            st.subheader("🗂️ Conserved Region Map")
            fig = plot_conserved_regions(alignment_result.get_alignment_length(), conserved_regions)
            st.pyplot(fig)

            st.subheader("📊 PDF Report")
            if st.button("🗓️ Generate PDF Report"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                    summary = {
                        "Number of Sequences": len(alignment_result),
                        "Alignment Length": alignment_result.get_alignment_length(),
                        "Threshold": threshold
                    }
                    plot_file = tmp_pdf.name.replace(".pdf", ".png")
                    fig.savefig(plot_file)
                    pdf_report.generate_pdf(tmp_pdf.name, summary, conserved_regions, snps, plot_file)
                    with open(tmp_pdf.name, "rb") as pdf_file:
                        st.download_button("Download PDF Report", data=pdf_file.read(), file_name="wheatconserve_report.pdf", mime="application/pdf")

        else:
            st.info("No conserved regions found at this threshold.")

        st.subheader("🧋 SNP Analysis")
        if snps:
            st.write(f"🔍 Found {len(snps)} SNP positions before filtering.")

            min_alleles = st.slider("🔍 Show SNPs with at least this many allele types:", 2, 5, 2)
            filtered_snps = [snp for snp in snps if len(snp["variation"]) >= min_alleles]

            st.write(f"🧪 Showing {len(filtered_snps)} SNPs with ≥ {min_alleles} allele types.")

            if filtered_snps:
                for snp in filtered_snps[:10]:
                    st.json(snp)

                snp_flat = []
                for snp in filtered_snps:
                    row = {"Position": snp["position"]}
                    for base, ids in snp["variation"].items():
                        row[base] = ", ".join(ids)
                    snp_flat.append(row)

                df_snps = pd.DataFrame(snp_flat)
                csv_snps = df_snps.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ Download SNPs CSV", csv_snps, "snp_analysis_filtered.csv", "text/csv")

                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df_snps.to_excel(writer, index=False, sheet_name="SNPs")
                st.download_button("⬇️ Download SNPs Excel", data=output.getvalue(), file_name="snp_analysis_filtered.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

                st.subheader("🧪 Primer Design for SNPs")
                reference_seq = str(alignment_result[0].seq).replace("-", "")
                primer_results = []
                primer_len = 20
                flank = 100
                for snp in filtered_snps[:10]:
                    pos = snp["position"]
                    if pos < flank or pos + flank > len(reference_seq):
                        continue
                    flanking_seq = reference_seq[pos - flank: pos + flank + 1]
                    primer_fwd = flanking_seq[flank:flank + primer_len]
                    primer_rev = str(Seq(flanking_seq[flank - primer_len:flank]).reverse_complement())
                    primer_results.append({
                        "SNP Position": pos,
                        "Flanking Sequence": flanking_seq,
                        "Primer Forward": primer_fwd,
                        "Primer Reverse": primer_rev
                    })
                if primer_results:
                    df_primers = pd.DataFrame(primer_results)
                    st.dataframe(df_primers)
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        df_primers.to_excel(writer, index=False, sheet_name="Primers")
                    st.download_button("⬇️ Download Primers (Excel)", data=output.getvalue(), file_name="snp_primers.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                else:
                    st.info("❗ No suitable SNPs for primer design (too close to edges).")

                st.subheader("📍 SNP Distribution Plot")
                snp_positions = [snp["position"] for snp in filtered_snps]
                allele_counts = [len(snp["variation"]) for snp in filtered_snps]
                fig_snp_dist, ax_snp_dist = plt.subplots(figsize=(10, 2))
                scatter = ax_snp_dist.scatter(snp_positions, [1]*len(snp_positions), c=allele_counts, cmap="viridis", s=20)
                ax_snp_dist.set_yticks([])
                ax_snp_dist.set_xlabel("Alignment Position")
                ax_snp_dist.set_title("Distribution of Filtered SNPs (colored by allele count)")
                plt.colorbar(scatter, ax=ax_snp_dist, label="# Alleles")
                st.pyplot(fig_snp_dist)
            else:
                st.warning("⚠️ No SNPs matched the selected allele filter.")
        else:
            st.info("No SNPs found.")

        st.subheader("🔍 BLAST Analysis")
        sequence_to_blast = str(alignment_result[0].seq).replace("-", "")
        blast_results = blast_analysis.run_blast(sequence_to_blast)

        if blast_results:
            for result in blast_results:
                st.write(f"Title: {result['title']}, E-value: {result['e_value']}, Score: {result['score']}")
        else:
            st.warning("No results found in BLAST search.")

    except Exception as e:
        st.error(f"❌ Error during alignment: {str(e)}")
else:
    st.warning("📂 Please upload a FASTA file to begin analysis.")
