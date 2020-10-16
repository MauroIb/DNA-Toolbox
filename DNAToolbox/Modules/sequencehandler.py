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
        
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)

        self.leftpanel = tk.Frame(self, borderwidth = 5, relief = tk.RIDGE)
        self.rightpanel = tk.Frame(self)

        self.leftpanel.grid(column = 0, row =0, sticky=(tk.N, tk.S, tk.E))
        self.rightpanel.grid(column = 1, row =0, sticky=(tk.N, tk.S, tk.W))
        ## Boton inicio
        title_label = tk.Label(self.leftpanel, text="Sequence Manager")
        title_label.grid(column = 0, row = 0)
        return_button = tk.Button(self.leftpanel, text="Back to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.grid(column = 10, row = 0)

        ## Carga de archivo local

        #options
        formatlist = ["fasta", "genbank", "swiss", "embl"]
        Combo = ttk.Combobox(self.leftpanel, values = formatlist)
        Combo.set("Tipo de archivo")
        Combo.grid(column = 10, row = 10)

        #button
        button_loadseq = tk.Button(self.leftpanel, text="Choose file for upload",
                           command=lambda: self.seq_from_file(Combo.get()))
        button_loadseq.grid(column = 0, row = 10)

        ## Carga de secuencia directa

        seq_entry = tk.Entry(self.leftpanel, width = 50)
        seq_entry.insert(0,'Paste your sequence here')
        seq_entry.grid(column = 0, row = 30, columnspan = 20)

        seq_entry_button = tk.Button(self.leftpanel, text="Load sequence manually",
                           command=lambda: self.seq_from_string(seq_entry.get()))
        seq_entry_button.grid(column = 0, row = 40)

        ## panel
        seqinspector_button = tk.Button(self.leftpanel, text="Open seq inspector",
                            command= lambda: self.seq_inspector())
        seqinspector_button.grid(row = 40, column = 10)


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
        seq_inspector_widget = ttk.Treeview(self.rightpanel, columns=('size', 'id',))
        seq_inspector_widget.column('size', width=100, anchor='center')
        seq_inspector_widget.heading('size', text='Size')
        seq_inspector_widget.column('id', width=100, anchor='center')
        seq_inspector_widget.heading('id', text='id')
        for item in self.records:
            seq_inspector_widget.insert('', 'end', text=item[:50], values=(len(item)," ") )
        seq_inspector_widget.pack(side=tk.RIGHT)


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
