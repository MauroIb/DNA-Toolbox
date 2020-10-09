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
