# Complete DNA Analyzer - Day 1 + Day 2 Combined

def analyze_dna(dna):
    
    # Clean input
    dna = dna.upper().replace(" ", "")
    
    print("=" * 45)
    print("       COMPLETE DNA ANALYSIS REPORT")
    print("=" * 45)
    
    # Basic info
    print("Sequence     :", dna)
    print("Length       :", len(dna), "bases")
    print()
    
    # Nucleotide counts (Day 1)
    print("--- NUCLEOTIDE COMPOSITION ---")
    print("A count :", dna.count("A"))
    print("T count :", dna.count("T"))
    print("G count :", dna.count("G"))
    print("C count :", dna.count("C"))
    print()
    
    # GC content (Day 2)
    gc = round((dna.count("G") + dna.count("C")) / len(dna) * 100, 2)
    print("--- GC CONTENT ---")
    print("GC Content   :", gc, "%")
    
    if gc > 60:
        print("Interpretation: High GC — very stable DNA 🔴")
    elif gc < 40:
        print("Interpretation: Low GC — less stable DNA 🔵")
    else:
        print("Interpretation: Normal GC range 🟢")
    
    print("=" * 45)

# Run it
analyze_dna("ATGCATGCTTAAGCCTTAGCGCGGCATGCAA")
