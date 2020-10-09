import Bio
from Bio.Seq import Seq
from Bio import SeqIO
import tkinter as tk
import interface

#frame con interfaz
def screen(frame):
    tk.Label(frame, text='A').pack()
    tk.Button(frame, text='Back to Main',
              command=lambda: interface.interface.goto('main', frame)).pack()

# returns seq record obj
def seq_from_file(f_string, f_option):
    records = list(SeqIO.parse(f_string, f_option))
    main = SeqIO.read(f_string, f_option)
    #si quiero la secuencia hago secuencia = main.seq
    return records

#returns seq obj
def seq_from_string(p_string):
    mainSeq = Seq(p_string)
    return mainSeq


## INTERFAZ - INPUT DE SECUENCIAS

seq_han_options = ("fasta", "genbank", "swiss", "embl")

#DROPDOWN MENU ELIGE SEQ_HAN_OPTIONS
#INPUT BOX PARA DAR PATH
#boton
def inputfileButton():
    #seqFromFile(path, seq_han_options)
    pass

#INPUT BOX PARA pegar secuencia
#boton
def inputStringButton():
    #seqFromString(string)
    pass




if __name__ == "__main__":
    
    pass
