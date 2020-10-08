import tkinter

# inicio
window = tkinter.Tk()
window.title("Falsa Web")
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
