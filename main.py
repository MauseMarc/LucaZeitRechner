import tkinter as tk
from tkinter import messagebox

def minMax(morning, mid, midend):
        check = [morning, mid, midend]
        for test in check:
            if not validateTime(test):
                return False
        morningTime = validateTime(mid) - validateTime(morning)
        workTimes=[492,540]
        dayFinish=[]
        for minmax in workTimes:
            workHours = minmax - morningTime
            workHours += validateTime(midend)
            workHours = convertMinutes(workHours)
            dayFinish.append(workHours)
        return dayFinish

def validateTime(time):
    valTime=[]
    if ":" in time or "," in time or "." in time:
        time=time.replace(" ",":").replace(",",":").replace(".",":")
        valTime=time.split(":")
    elif len(time) == 3 or len(time) == 4:
            valTime.append(time[:-2])
            valTime.append(time[-2:])
    else:
        return False
    if valTime[0].isdigit() and valTime[1].isdigit():
        valTime[0]=int(valTime[0])
        valTime[1]=int(valTime[1])
    else:
        return False
    if valTime[0] >23 or valTime[1] >59:
        return False
    minuteTime=valTime[0]*60+valTime[1]
    return minuteTime

def convertMinutes(totalMinutes):
    overspill = totalMinutes % 60
    hour = (totalMinutes - overspill) / 60
    return int(hour),overspill

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

        self.lbl1 = tk.Label(text="")
        self.lbl1.pack(pady=10)

        self.lbl2 = tk.Label(text="")
        self.lbl2.pack(pady=10)

    def calc_time(self):
        start_time = self.starttime.get(1.0, "end-1c")
        mittag_start = self.mittag_start.get(1.0, "end-1c")
        mittag_end = self.mittag_end.get(1.0, "end-1c")
        min_max_time = minMax(start_time, mittag_start, mittag_end)
        if not min_max_time:
            messagebox.showinfo(title="Fehler", message="Zeiteingabe ungültig")
        else:
            min_time_t = min_max_time[0]
            max_time_t = min_max_time[1]
            min_time = f"{min_time_t[0]:02}:{min_time_t[1]:02}"
            max_time = f"{max_time_t[0]:02}:{max_time_t[1]:02}"

            self.lbl1.configure(text=f"Minimale Zeit: {min_time}")
            self.lbl2.configure(text=f"Maximale Zeit: {max_time}")

def main():
    root = tk.Tk()
    app = App(root)
    root.geometry("300x400")
    root.mainloop()

if __name__ == "__main__":
    main()