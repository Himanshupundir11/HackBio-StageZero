"""
Enhanced GC Content Calculator

This script calculates the GC content of a DNA sequence and includes:
- Input validation
- Handling of unknown bases (N)
- Support for FASTA-style sequences
- Function documentation and improved readability
"""

def gc_content(sequence: str) -> float:
    """
    Calculate GC content percentage of a DNA sequence.

    Parameters:
        sequence (str): DNA sequence (ATGC characters). Can include lowercase.

    Returns:
        float: Percent GC content (0-100)
    """

    # Remove FASTA header if present
    if sequence.startswith(">"):
        sequence = "".join(sequence.split("\n")[1:])

    # Clean sequence
    sequence = sequence.upper().replace("\n", "").strip()

    # Count only valid bases
    valid_bases = [base for base in sequence if base in ["A", "T", "G", "C"]]

    if len(valid_bases) == 0:
        raise ValueError("Sequence contains no valid DNA bases (A, T, G, C)")

    g = valid_bases.count("G")
    c = valid_bases.count("C")
    gc_percentage = (g + c) / len(valid_bases) * 100

    return gc_percentage

# Example usage
dna_sequence = "ATGCGCATTAACCGG"
print(f"GC content: {gc_content(dna_sequence):.2f}%")
