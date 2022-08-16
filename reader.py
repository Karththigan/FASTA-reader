from fasta import FASTA

def main():
    fasta_one = FASTA("rosalind_gc.txt")
    print(fasta_one.aa_content(basepairs=["G","C"]))

if __name__ == "__main__":
    main()