import tkinter as tk
from sequencehandler import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #Container. The one on top is visible
        for F in (StartPage, SequenceHandlerScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")

    def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pagina Principal")
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Open Sequence Handler",
                            command=lambda: controller.show_frame("SequenceHandlerScreen"))
        button1.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
