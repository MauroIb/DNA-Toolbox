import Bio
from Bio.Seq import Seq
from Bio import SeqIO

def seq_from_file(f_string, f_option):
    records = list(SeqIO.parse("ls_orchid.gbk", "genbank"))
    return records

def seq_from_string(p_string):
    mainSeq = Seq(p_string)
    return mainSeq



