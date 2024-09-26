from TimeCalcModule import *
from WorkTimeCalc import *
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        root.title("Arbeitszeitrechner")

        self.inputtxt = tk.Text(height= 1, width= 10)
        self.inputtxt.pack(pady=10)

        self.button = tk.Button(root, text="print", command=self.printt)
        self.button.pack(pady=10)

        self.lbl = tk.Label(text="")
        self.lbl.pack(pady=10)
    
    def printt(self):
        input_text = self.inputtxt.get(1.0, "end-1c")
        self.lbl.config(text=input_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("300x400")
    root.mainloop()