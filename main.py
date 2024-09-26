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

        self.button = tk.Button(root, text="print", command=self.calc_time)
        self.button.pack(pady=10)

        self.lbl = tk.Label(text="")
        self.lbl.pack(pady=10)

    def calc_time(self):
        start_time = self.starttime.get(1.0, "end-1c")
        mittag_start = self.mittag_start.get(1.0, "end-1c")
        mittag_end = self.mittag_end.get(1.0, "end-1c")
        min_max_time = minMax(start_time, mittag_start, mittag_end)
        min_time = 

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("300x400")
    root.mainloop()