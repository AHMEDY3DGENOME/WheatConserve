import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import tempfile

from modules import alignment, conserved, snp_analysis, pdf_report

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
This tool performs multiple sequence alignment, highlights conserved regions, and detects SNPs.
""")

uploaded_file = st.file_uploader("Upload a FASTA file with multiple sequences", type=["fasta", "fa", "txt"])

if uploaded_file is not None:
    with open("temp_input.fasta", "wb") as f:
        f.write(uploaded_file.read())

    try:
        st.success("✅ File uploaded successfully. Running alignment...")

        alignment_result = alignment.run_alignment("temp_input.fasta")

        st.subheader("📊 Alignment Summary")
        st.text(f"Number of sequences: {len(alignment_result)}")
        st.text(f"Alignment length: {alignment_result.get_alignment_length()}")

        st.subheader("🧬 Aligned Sequences (First 300 bases)")
        for record in alignment_result:
            st.text(f">{record.id}\n{record.seq[:300]}...")

        #  SNP
        snps = snp_analysis.find_snps(alignment_result)

        # Conversed Regions
        st.subheader("🟩 Conserved Regions")
        threshold = st.slider("Select conservation threshold", 0.5, 1.0, 0.9, 0.05)
        conserved_regions = conserved.find_conserved_regions(alignment_result, threshold)

        if conserved_regions:
            for region in conserved_regions:
                st.write(f"Region: {region[0]} - {region[1]}")

            #  CSV
            df_conserved = pd.DataFrame(conserved_regions, columns=["Start", "End"])
            csv_conserved = df_conserved.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Conserved Regions CSV", csv_conserved, "conserved_regions.csv", "text/csv")

            # Charts
            st.subheader("🖼️ Conserved Region Map")
            fig = plot_conserved_regions(alignment_result.get_alignment_length(), conserved_regions)
            st.pyplot(fig)
            #PDF REPORT
            if st.button("📄 Generate PDF Report"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    summary = {
                        "Number of Sequences": len(alignment_result),
                        "Alignment Length": alignment_result.get_alignment_length(),
                        "Threshold": threshold
                    }
                    plot_file = tmp.name.replace(".pdf", ".png")
                    fig.savefig(plot_file)

                    pdf_report.generate_pdf(tmp.name, summary, conserved_regions, snps, plot_file)

                    with open(tmp.name, "rb") as pdf_file:
                        st.download_button(
                            label="📥 Download PDF Report",
                            data=pdf_file.read(),
                            file_name="wheatconserve_report.pdf",
                            mime="application/pdf"
                        )
        else:
            st.info("No conserved regions found at this threshold.")

        # SNP Analysis Section
        st.subheader("🧬 SNP Analysis")
        if snps:
            st.write(f"🔍 Found {len(snps)} SNP positions.")
            for snp in snps[:10]:
                st.json(snp)

            snp_flat = []
            for snp in snps:
                row = {"Position": snp["position"]}
                for base, ids in snp["variation"].items():
                    row[base] = ", ".join(ids)
                snp_flat.append(row)

            df_snps = pd.DataFrame(snp_flat)
            csv_snps = df_snps.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download SNPs CSV", csv_snps, "snp_analysis.csv", "text/csv")

        else:
            st.info("No SNPs found.")

    except Exception as e:
        st.error(f"❌ Error during alignment: {str(e)}")

else:
    st.warning("📂 Please upload a FASTA file to begin analysis.")
