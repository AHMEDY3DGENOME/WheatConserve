from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def generate_pdf(filename, summary, conserved_regions, snps, plot_path=None):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 2 * cm

    def write_line(text, font="Helvetica", size=11):
        nonlocal y
        if y < 2 * cm:
            c.showPage()
            y = height - 2 * cm
        c.setFont(font, size)
        c.drawString(2 * cm, y, text)
        y -= 15

    write_line("WheatConserve Report", "Helvetica-Bold", 14)
    write_line(" ")

    for key, value in summary.items():
        write_line(f"{key}: {value}")
    write_line(" ")

    # Conserved Regions
    write_line("Conserved Regions", "Helvetica-Bold", 12)
    if conserved_regions:
        for start, end in conserved_regions:
            write_line(f"• {start} - {end}")
    else:
        write_line("No conserved regions found.")

    write_line(" ")

    # SNPs
    write_line("SNPs", "Helvetica-Bold", 12)
    if snps:
        for snp in snps[:20]:
            variations = "; ".join([f"{b}: {', '.join(ids)}" for b, ids in snp["variation"].items()])
            write_line(f"• Pos {snp['position']}: {variations}")
    else:
        write_line("No SNPs found.")

    write_line(" ")

    if plot_path:
        try:
            c.drawImage(plot_path, 2 * cm, y - 180, width=16 * cm, height=4 * cm)
        except:
            write_line("[Error loading plot image]")

    c.save()
