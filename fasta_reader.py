class FASTA:
    """
    
    """
    def __init__(self, sequencetextfile):
        self.file = sequencetextfile
        with open(self.file, "r") as f:
            name_and_seq = {}
            info = f.readlines()
            name_indices = []

        for i in range(len(info)):
            info[i] = info[i].rstrip()
            if info[i][0] == ">":
                name_indices.append(i)

        name_indices.append(len(info))
        
        #create dictionary with key = Taxon, value = sequence
        for index in name_indices[:-1]:
            if index == name_indices[-2]:
                name_and_seq[info[index].replace(">","")] = "".join(info[index + 1:name_indices[-1]])
            else:
                name_and_seq[info[index].replace(">","")] = "".join(info[index + 1: name_indices[name_indices.index(index) + 1]])
        
        self.taxa = name_and_seq.keys()
        self.keys = name_and_seq.values()
    
    def __str__(self) -> str:
        return f"FASTA of {self.file}"
    
    def __repr__(self) -> str:
        return f"FASTA.{self.file}"
    
    def aa_content(self, basepairs):
        """Return the percentage of specific bases contianed in a nucleic acid sequence
        
        Arguments:
            basepair: list containing bases to search for in sequence

        Return:
            aa: List containing amount (in percentage) of basepairs in basepair in each sequence
        """
        pass
        aa = []

        for seq in self.keys:
            seq_length = len(seq)
            aa_content = 0
            for base in seq:
                if base in basepairs:
                    aa_content += 1

            aa.append(100 * aa_content / len(seq))

        return aa
    def get_sequence(self,seq_label):
        """
        Return specific sequence from FASTA file given defline

        Arguments:
            seq_label: defline of specific sequence
        Return:
            sequence: string containing nucleic acid sequence
        """
        for defline in self.taxa:
            if defline == seq_label:
                return list(self.keys)[list(self.taxa).index(defline)]
    

    


def main():
    fasta_one = FASTA("rosalind_gc.txt")
    # print(list(fasta_one.taxa))
    # AT_content = fasta_one.aa_content(["A", "T", "C"])
    # print(AT_content)
    # print(len(fasta_one.taxa), len(AT_content))
    print(fasta_one.get_sequence("Rosalind_6363"))

if __name__ == "__main__":
    main()