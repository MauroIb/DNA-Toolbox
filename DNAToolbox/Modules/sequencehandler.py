import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import interface
import time


class SequenceHandlerScreen(tk.Frame):
    def __init__(self, parent, controller):
        #### FUNCIONAMIENTO INTERNO
        self.records = []
        
    ################# INTERFAZ
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        ### General y back button
        title_label = tk.Label(self, text="Sequence Manager")
        title_label.grid(column = 0, row = 0)
        return_button = tk.Button(self, text="Back to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        return_button.grid(column = 1, row = 0)

        self.columnconfigure(0, weight = 0)
        self.columnconfigure(1, weight = 1)
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)

        self.leftpanel = tk.Frame(self, borderwidth = 5, relief = tk.RIDGE)
        self.rightpanel = tk.Frame(self)

        self.leftpanel.grid(column = 0, row =1, sticky=(tk.N, tk.W, tk.S))
        self.rightpanel.grid(column = 1, row =1, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.drawLeftPanel()
        self.drawRightPanel()

    ################################ LEFT PANEL

    def drawLeftPanel(self):

        ############## Carga de archivo local
        #---options
        load_file_label = tk.Label(self.leftpanel, text= "Load file locally", pady=5)
        load_file_label.grid(row=9, column=0)
        formatlist = ["fasta", "genbank", "swiss", "embl"]
        Combo = ttk.Combobox(self.leftpanel, values = formatlist)
        Combo.set("genbank")
        Combo.grid(column = 10, row = 10)

        #---button
        button_loadseq = tk.Button(self.leftpanel, text="Choose file for upload",
                           command=lambda: self.seq_from_file(Combo.get()))
        button_loadseq.grid(column = 0, row = 10)

        #--- Break
        separator = ttk.Separator(self.leftpanel, orient = tk.HORIZONTAL)
        separator.grid(column = 0, row = 15, columnspan = 100, sticky = (tk.W, tk.E),  pady = 10)
        
        ############## Carga de secuencia directa
        seq_entry_label = tk.Label(self.leftpanel, text = "Or paste your sequence here:")
        seq_entry_label.grid(row=20, column =0)
        
        #---ID
        seq_id_label = tk.Label(self.leftpanel, text = "ID:", pady=5, anchor = tk.E)
        seq_id_label.grid(row=28, column =0)
        seq_id_entry = tk.Entry(self.leftpanel, width = 10)
        seq_id_entry.grid(row = 28, column = 1, padx = 5)

        #---NAME
        seq_name_label = tk.Label(self.leftpanel, text = "Name:", pady=5)
        seq_name_label.grid(row=28, column =9)
        seq_name_entry = tk.Entry(self.leftpanel, width = 10)
        seq_name_entry.grid(row = 28,column = 10, padx = 5)
        
        #---DESCRIPTION
        seq_descr_label = tk.Label(self.leftpanel, text = "Description", pady=5)
        seq_descr_label.grid(row=29, column =0)
        seq_descr_entry = tk.Entry(self.leftpanel, width = 10)
        seq_descr_entry.grid(row = 29,column = 1,  columnspan = 10, sticky = (tk.W, tk.E), padx = 5)

        #---SEQUENCE
        seq_entryfield_label = tk.Label(self.leftpanel, text = "Sequence", pady=5)
        seq_entryfield_label.grid(row=30, column =0, columnspan = 20)
        seq_entry = tk.Text(self.leftpanel, width = 50, height = 20)
        seq_entry.grid( row = 31, column = 0, columnspan = 20, sticky = (tk.N, tk.S))

        self.leftpanel.rowconfigure(31, weight = 1)

        ###############  PANEL

        #---DO
        seq_entry_button = tk.Button(self.leftpanel, text="Load sequence manually",
                           command=lambda: self.seq_from_string(seq_entry.get("1.0","end-1c"),
                           seq_id_entry.get(), seq_name_entry.get(), seq_descr_entry.get()))
        seq_entry_button.grid(column = 0, row = 40)

        #---UNDO
        undo_button = tk.Button(self.leftpanel, text="Undo Insert",
                            command= lambda: self.records.pop())
        undo_button.grid(row = 40, column = 4)



        #---CLEARMEM
        clearmemory_button = tk.Button(self.leftpanel, text="Clear Memory",
                            command= lambda: self.records.clear())
        clearmemory_button.grid(row = 40, column = 5)

        #---REFRESH
        seqinspector_button = tk.Button(self.leftpanel, text="Update Seq Inspector",
                            command= lambda: self.drawRightPanel())
        seqinspector_button.grid(row = 40, column = 10)

    ######################## REG INSPECTOR

    def drawRightPanel(self):
        #clear for update
        for widget in self.rightpanel.winfo_children():
            widget.destroy()

        ## tree object
        
        self.rightpanel.columnconfigure(0, weight = 1)
        self.rightpanel.rowconfigure(0, weight = 1)

        columns = ('id','size','features', 'description', 'sample')

        reg_inspector_w = ttk.Treeview(self.rightpanel, columns=columns, selectmode = 'extended')

        reg_inspector_w.column('#0', width=100, anchor='center')
        reg_inspector_w.column('id', width=100, anchor='center')
        reg_inspector_w.column('size', width=50, anchor='center')
        reg_inspector_w.column('features', width=50, anchor='center')
        reg_inspector_w.column('description', width=300, anchor='center')
        reg_inspector_w.column('sample', width=200, anchor='center')

        for col in columns: 
            reg_inspector_w.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(
                reg_inspector_w, _col, False))

        # read records
        for record in self.records:
            reg_inspector_w.insert('', 'end', text=record.name, iid =record.id,
                values=(record.id, len(record.seq), len(record.features), record.description,  record.seq[:50]))

        reg_inspector_w.grid(row=0, column=0,  sticky=(tk.N, tk.S, tk.E, tk.W))

        #---REMOVE ITEM
        delete_button = tk.Button(self.rightpanel, text="Remove Item",
                            command= lambda: self.removeItem(reg_inspector_w.focus()))
        delete_button.grid(row = 1, column = 0)

    ############ Read from file
 
    def removeItem(self, iid):
        for pos , record in enumerate(self.records):
            if record.id == iid: self.records.pop(pos)
        self.drawRightPanel()

    def seq_from_file(self, f_option):
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                        filetypes=(("txt files", "*.txt"),("all files", "*.*")))
        if path:
            for record in SeqIO.parse(path, f_option):
                self.records.append(record)
        self.drawRightPanel()

    ############ Build from fields

    def seq_from_string(self, p_seq, p_id, p_name, p_description):
        if p_id == '': p_id = str(int(time.time()))
        new_record = SeqRecord(
            Seq(p_seq),
            id=p_id,
            name=p_name,
            description=p_description,
            )
        self.records.append(new_record)
        self.drawRightPanel()

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        tv.heading(col, command=lambda _col=col: self.treeview_sort_column(tv, _col, not reverse))


if __name__ == "__main__":
    
    pass
