<<<<<<< HEAD
import tkinter as tk
import sequencehandler

class Interface():
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x500')
        frame = tk.Frame(self.master)
        frame.pack()
        self.main(frame)

    def begin(self):
        root = tk.Tk()
        window = Interface(root)
        root.mainloop()

    def goto(self, destination, frame):
        frame.destroy()
        frame = tk.Frame(self.master)
        frame.pack()
        goto = {
            'main': self.main,
            'seqHandler': sequencehandler.screen,
        }
        goto[destination](frame)

    def main(self, frame):
        tk.Label(frame, text='Main').pack()
        tk.Button(frame, text='Goto A', command=lambda: self.goto('seqHandler', frame)).pack()


if __name__ == '__main__':
        root = tk.Tk()
        window = Interface(root)
        root.mainloop()
=======
import tkinter

def startInterface():
    window.mainloop()

# inicio
window = tkinter.Tk()
window.title("Falsa Web hdfsakjsf")
window.geometry('800x600')

#label
labelTx = tkinter.Label(window,text="LABEL1")
labelTx.grid(column=0,row=0)

#field
Tx_Etiqueta = tkinter.Entry(window, width=12)
Tx_Etiqueta.insert(0,"Seq")
Tx_Etiqueta.grid(column=1,row=1)
Tx_Etiqueta_lb = tkinter.Label(window,text="Sequence")
Tx_Etiqueta_lb.grid(column=0,row=1)

# f boton
def clickedButton():
    pass

#boton
bt= tkinter.Button(window,text="EJECUTAR", command = clickedButton)
bt.grid(column=1,row=7)


if __name__ == "__main__":
   window.mainloop()
>>>>>>> 605839deba1a15f48562bad62a6849942b77318d
