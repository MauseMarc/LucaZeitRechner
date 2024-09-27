<<<<<<< Updated upstream
def minToHour(minutes):
    calc = minutes % 60
    minut = calc
    hour = int((minutes - calc) / 60)
    return hour,"Uhr",minut,"Minuten"


# running=True
# while running:
#     start=input("Start Time: ")
#     mittag=input("Mittagpause Start: ")
#     nachmittag=input("Mittagpause Ende: ")
#
#     minwork=(8*60)+12
#
#     s1=int(start[:2])*60
#     s2=(int(start[2:]))
#
#     m1=int(mittag[:2])*60
#     m2=(int(mittag[2:]))
#
#     n1=int(nachmittag[:2])*60
#     n2=(int(nachmittag[2:]))
#
#     s=s1+s2
#     m=m1+m2
#     n=n1+n2
#
#     morning=m-s
#     difference=minwork - morning
#     maxifference=(9*60)-morning
#
#     end=n + difference
#     maxend=n + maxifference
#     print(minToHour(end))
#     print(minToHour(maxend),"Max!")
#     que= input("ERGH")
#     if que.lower()=="y":
#         running=False




print("I commited changes to the federal law of switzerland")
print("Hello world")
print("this should be a branceh")
=======
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

def wait(minMaxEnd):
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
>>>>>>> Stashed changes
