from TimeCalcModule import *
import time
import datetime
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

def show_popup():
    root=tk.Tk()
    root.lift()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo("Popup", "Arbeitszeit minimum erreicht!")
    root.destroy()

def displayLeaveAlarm(minMaxEnd):
    now = datetime.datetime.now()
    conversion=str(now.time())
    currentTime=conversion.split(":")
    seconds= currentTime[-1].split(".")
    seconds=int(seconds[0])
    currentTime=currentTime[:-1]

    nowTime=int(currentTime[0])*60+int(currentTime[1])
    endTime=minMaxEnd[0]*60+minMaxEnd[1]

    waitTime=(endTime-nowTime)*60-seconds
    print("alarm will appear in",int((waitTime-waitTime%60)/60),"minutes and",waitTime%60,"seconds")

    if waitTime < 1:
        return False
    else:
        time.sleep(waitTime)
        show_popup()