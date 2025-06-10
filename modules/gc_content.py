from Bio.SeqUtils import gc_fraction

# gc_content.py - fix
def calculate_gc_content(alignment):
    results = []
    for record in alignment:
        gc = gc_fraction(record.seq) * 100
        results.append({
            "id": record.id,
            "length": len(record.seq),
            "gc_content": round(gc, 2)
        })
    return results
