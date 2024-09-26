import datetime
import time
from TimeCalcModule import *

def input_time():
    start_time = input("Start Time: ")
    mittag_start = input("Mittag Start: ")
    mittag_ende = input("Mittag Ende: ")
    return start_time, mittag_start, mittag_ende

s, m, n = input_time()

start, start_min = validateTime(s)
mittag_start, mittag_start_min = validateTime(m)
mittag_ende, mittag_ende_min = validateTime(n)

def calc_time_delta(start, ende):
    return ende - start

minwork = 492
maxwork = 540

morning_time = calc_time_delta(start_min, mittag_start_min)

minwork_n = minwork - morning_time
maxwork_n = maxwork - morning_time

minwork_min = minwork_n + mittag_ende_min
maxwork_min = maxwork_n + mittag_ende_min

minwork_h = convertMinutes(minwork_min)
maxwork_h = convertMinutes(maxwork_min)

print(minwork_h, maxwork_h)
