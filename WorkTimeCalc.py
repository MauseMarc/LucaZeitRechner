from TimeCalcModule import *


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




x = minMax("752","1146","1222")
print(x)







# if __name__ == "__main__":
#     def minMax():
#         s, m, n = input_time()
#         try:
#             start, start_min = validateTime(s)
#             mittag_start, mittag_start_min = validateTime(m)
#             mittag_ende, mittag_ende_min = validateTime(n)
#
#             minwork = 492
#             maxwork = 540
#
#             morning_time = mittag_start_min - start_min
#
#             minwork_n = minwork - morning_time
#             maxwork_n = maxwork - morning_time
#
#             minwork_min = minwork_n + mittag_ende_min
#             maxwork_min = maxwork_n + mittag_ende_min
#
#             minwork_h = convertMinutes(minwork_min)
#             maxwork_h = convertMinutes(maxwork_min)
#
#             print(minwork_h, maxwork_h)
#         except Exception:
#             return False
