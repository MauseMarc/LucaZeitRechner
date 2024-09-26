import os
import time
import datetime
os.system("")


# def minToHour(minutes):
#     calc = minutes % 60
#     minut = calc
#     hour = int((minutes - calc) / 60)
#     return hour,"Uhr",minut,"Minuten"


# running=True
# while running:
#     start=input("Start Time: ")
#     mittag=input("Mittagpause Start: ")
#     nachmittag=input("Mittagpause Ende: ")

#     minwork=(8*60)+12

#     s1=int(start[:2])*60
#     s2=(int(start[2:]))

#     m1=int(mittag[:2])*60
#     m2=(int(mittag[2:]))

#     n1=int(nachmittag[:2])*60
#     n2=(int(nachmittag[2:]))

#     s=s1+s2
#     m=m1+m2
#     n=n1+n2

#     morning=m-s
#     difference=minwork - morning
#     maxifference=(9*60)-morning

#     end=n + difference
#     maxend=n + maxifference
#     print(minToHour(end))
#     print(minToHour(maxend),"Max!")
#     que= input("ERGH")
#     if que.lower()=="y":
#         running=False

def input_time():
    start_time = input("Start Time: ")
    mittag_start = input("Mittag Start: ")
    mittag_ende = input("Mittag Ende: ")
    validate_time(start_time)
    validate_time(mittag_start)
    validate_time(mittag_ende)
    return start_time, mittag_start, mittag_ende

# def time_calc():
#     s=s1+s2
#     m=m1+m2
#     n=n1+n2

#     morning=m-s
#     difference=minwork - morning
#     maxifference=(9*60)-morning

#     end=n + difference
#     maxend=n + maxifference
#     print(minToHour(end))
#     print(minToHour(maxend),"Max!")


def validate_time(time):
    time_format = "%H:%M"
    try:
        validtime = datetime.datetime.strptime(time, time_format)
        return True
    except ValueError:
        return False

def normalize_time(time):
    time_normalized = time.replace(":", "")
    return time_normalized

def separate_time(time):
    time_norm = normalize_time(time)
    a = time_norm[0:2]
    b = time_norm[2:4]
    return a, b

s, m, n = input_time()

s_hour, s_min = separate_time(s)
m_hour, m_min = separate_time(m)
n_hour, n_min = separate_time(n)

def calc_time_delta(hours, min):
    time_delta = datetime.timedelta(hours= + float(hours), minutes= + float(min))
    return time_delta

print(calc_time_delta((float(m_hour) - float(s_hour)), (float(m_min) - float(s_min))))

# print("I commited changes to the federal law of switzerland")
# print("Hello world")