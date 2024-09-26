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