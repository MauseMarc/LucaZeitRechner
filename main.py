import tkinter as tk
from tkinter import messagebox
from WorkTimeCalc import *
import time
from tkinter import messagebox
class App:
    def __init__(self, root):
        self.root = root
        root.title("Arbeitszeitrechner")

        self.starttime_title = tk.Label(root, text="Startzeit eingeben")
        self.starttime_title.pack(pady=1)

        self.starttime = tk.Entry()
        self.starttime.pack(pady=1)

        self.mittag_start_title = tk.Label(root, text="Mittag Start eingeben")
        self.mittag_start_title.pack(pady=1)

        self.mittag_start = tk.Entry()
        self.mittag_start.pack(pady=1)

        self.mittag_end_title = tk.Label(root, text="Mittag Ende eingeben")
        self.mittag_end_title.pack(pady=1)

        self.mittag_end = tk.Entry()
        self.mittag_end.pack(pady=1)

        self.button = tk.Button(root, text="print", command=lambda:[self.calc_time()])
        self.button.pack(pady=10)
        
        self.notification = tk.IntVar()
        self.notification_switch = tk.Checkbutton(root, text="Benachrichtigung beim Erreichen der Zeit", variable=self.notification, onvalue=1, offvalue=0, command= self.update_notification_status)
        self.notification_switch.pack(pady=5)

        self.lbl1 = tk.Label(text="")
        self.lbl1.pack(pady=5)

        self.lbl2 = tk.Label(text="")
        self.lbl2.pack(pady=5)

        self.lbl3 = tk.Label(text="Benachrichtigung aus")
        self.lbl3.pack(pady=5)

        self.lbl4 =tk.Label(text="")
        self.lbl4.pack(pady=5)

        self.min_time = 0
        self.max_time = 0
        self.wait_time = 0
        self.popup_v = 0

    def calc_time(self):
        start_time = self.starttime.get()
        mittag_start = self.mittag_start.get()
        mittag_end = self.mittag_end.get()
        min_max_time = minMax(start_time, mittag_start, mittag_end)
        if not min_max_time:
            messagebox.showinfo(title="Fehler", message="Zeiteingabe ungültig")
        else:
            min_time_t = min_max_time[0]
            max_time_t = min_max_time[1]
            min_time = f"{min_time_t[0]:02}:{min_time_t[1]:02}"
            max_time = f"{max_time_t[0]:02}:{max_time_t[1]:02}"

            self.lbl1.configure(text=f"Minimale Zeit: {min_time}", bg="#B0BEC5")
            self.lbl2.configure(text=f"Maximale Zeit: {max_time}", bg="#B0BEC5")
            self.min_time = min_time
            self.max_time = max_time
            self.display_time_until_end()
            self.popup_v = 1

    def update_notification_status(self):
        if self.notification.get() == 0:
            self.lbl3.config(text="Benachrichtigung aus")
            return
        else:
            self.lbl3.config(text="Benachrichtigung ein")
            return
    
    def display_time_until_end(self):
        until_end, wait_time = time_until_end(self.min_time)
        self.lbl4.config(text=until_end)
        self.wait_time = wait_time
    
    def popup(self):
        wait_time = self.wait_time
        if wait_time < 1:
            return
        else:
            print("slep")
            time.sleep(wait_time)
            if self.notification == 1:    
                messagebox.showinfo("8:12 erreicht!")
    



def main():
    root = tk.Tk()
    app = App(root)
    root.geometry("300x500")
    root.mainloop()

if __name__ == "__main__":
    main()