from TimeCalcModule import *
from WorkTimeCalc import *
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        root.title("Arbeitszeitrechner")

        self.starttime_title = tk.Label(root, text="Startzeit eingeben")
        self.starttime_title.pack(pady=10)

        self.starttime = tk.Text(height= 1, width= 10)
        self.starttime.pack(pady=10)

        self.mittag_start_title = tk.Label(root, text="Mittag Start eingeben")
        self.mittag_start_title.pack(pady=10)

        self.mittag_start = tk.Text(height= 1, width= 10)
        self.mittag_start.pack(pady=10)

        self.mittag_end_title = tk.Label(root, text="Mittag Ende eingeben")
        self.mittag_end_title.pack(pady=10)

        self.mittag_end = tk.Text(width=10, height=1)
        self.mittag_end.pack(pady=10)

        self.button = tk.Button(root, text="print", command=self.printt)
        self.button.pack(pady=10)

        self.lbl = tk.Label(text="")
        self.lbl.pack(pady=10)
    
    def printt(self):
        input_text = self.starttime.get(1.0, "end-1c")
        self.lbl.config(text=input_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("300x400")
    root.mainloop()