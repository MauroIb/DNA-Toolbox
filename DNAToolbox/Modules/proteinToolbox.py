import Bio
import tkinter as tk
from Bio.Seq import Seq

#interfaz para interaccion
def draw_interface():
    pass

#transcripcion de secuencia
def transcribe(DNA_sequence):
    DNA_sequence = DNA_sequence.transcribe()
    protein_string = DNA_sequence.translate(stop_codon=true)
    proteins_split = protein_string.split("*")
    proteins_clean  = [str(i) for i in proteins_split]
    return proteins_clean





