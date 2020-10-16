import Bio
from Bio.Seq import Seq
from Bio import SeqIO
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import interface


class SequenceHandlerScreen(tk.Frame):
    def __init__(self, parent, controller):
        #### FUNCIONAMIENTO INTERNO
        self.records = []
        
        #### INTERFAZ
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ## Boton inicio
        tk.Label(self, text="Sequence Manager").pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        ## Carga de archivo local

        #options
        formatlist = ["fasta", "genbank", "swiss", "embl"]
        Combo = ttk.Combobox(self, values = formatlist)
        Combo.set("Tipo de archivo")
        Combo.pack(padx = 5, pady = 5)

        #button
        button_loadseq = tk.Button(self, text="Choose file for upload",
                           command=lambda: self.seq_from_file(Combo.get()))
        button_loadseq.pack()

        ## Carga de secuencia directa

        seq_entry = tk.Entry(self, width = 50)
        seq_entry.insert(0,'Paste your sequence here')
        seq_entry.pack(padx = 5, pady = 5)

        seq_entry_button = tk.Button(self, text="Load sequence manually",
                           command=lambda: self.seq_from_string(seq_entry.get()))
        seq_entry_button.pack()

        ## panel
        labelreport = "Number of sequences " + str(len(self.records))
        tk.Label(self, text=labelreport).pack(side="top", fill="x", pady=10)

        seqinspector_button = tk.Button(self, text="Open seq inspector",
                            command= lambda: self.seq_inspector())
        seqinspector_button.pack()


############

    def seq_from_file(self, f_option):
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                        filetypes=(("txt files", "*.txt"),("all files", "*.*")))
        if path:
            self.records = list(SeqIO.parse(path, f_option))
            #si quiero la secuencia hago secuencia = main.seq

    def seq_from_string(self, p_string):
        self.records.append(Seq(p_string))
        
    def seq_inspector(self):
        seq_inspector_widget = ttk.Treeview(self, columns=('size', 'id',))
        seq_inspector_widget.column('size', width=100, anchor='center')
        seq_inspector_widget.heading('size', text='Size')
        seq_inspector_widget.column('id', width=100, anchor='center')
        seq_inspector_widget.heading('id', text='id')
        for item in self.records:
            seq_inspector_widget.insert('', 'end', text=item[:50], values=(len(item)," ") )
        seq_inspector_widget.pack()


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
