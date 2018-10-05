def gc(dna):
    # This function computes the GC percentage of a dna sequence

    nbases = dna.count('n') + dna.count('N')  # This is to count the number of n bases
    gcpercent = (float(dna.count('c') + dna.count('g') + dna.count('C') + dna.count('G')) / (len(dna) - nbases) * 100)

    return gcpercent


def stop_codon(dna, frame=0):
    # This function checks if given DNA sequence has in frame stop codons."
    # The default frame is 0, but when calling the function you may specify 0, 1, or 2

    stop_codon_found = False  # we are going to say stop_codon_found is False so that when it is found it can be true
    stop_codons = ['tga', 'tag', 'taa']  # these are the three stop codons in all living organisms
    for i in range(frame, len(dna),3):  # so starting as position 0, going the entire length of the sequence, taking a step size of 3
        codon = dna[i:i + 3].lower() #
        if codon in stop_codons:
            print("Input sequence has an inframe stop codon.")
            stop_codon_found = True
            break
        else:
            print("Input sequence has no inframe stop codon")

    return stop_codon_found


def reverse_complement(seq):
    # Returns the reverse complement of the DNA string

    def reverse_string(seq):
        return seq[::-1]  # This is the extended slice syntax. The arguments are [begin:end:step].
        # We just leave the beginning and end as colons and use -1 as the step size which will reverse the string

    seq = reverse_string(seq)

    def complement(dna):
        # Return the complementary sequence string
        base_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a',
                          'n': 'n'}
        # We're just creating a dictionary with key value pairs for all the iterations that we may encounter in a DNA sequence
        letters = list(dna)  # This is converting the dna sequence into a list
        letters = [base_complement[base] for base in letters]
        return ''.join(letters)

    seq = complement(seq)
    return seq
