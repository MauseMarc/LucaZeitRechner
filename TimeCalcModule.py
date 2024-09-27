def validateTime(myTime):
    valTime=[]
    if ":" in myTime or "," in myTime or "." in myTime:
        myTime=myTime.replace(" ",":").replace(",",":").replace(".",":")
        valTime=myTime.split(":")
    elif len(myTime) == 3 or len(myTime) == 4:
            valTime.append(myTime[:-2])
            valTime.append(myTime[-2:])
    else:
        return False

    if valTime[0].isdigit() and valTime[1].isdigit():
        valTime[0]=int(valTime[0])
        valTime[1]=int(valTime[1])
    else:
        return False
    if valTime[0] >23:
        return False
    if valTime[1] >59:
        return False
    minuteTime=valTime[0]*60+valTime[1]
    return valTime,minuteTime


def convertMinutes(totalMinutes):
    overspill = totalMinutes % 60
    hour = (totalMinutes - overspill) / 60
    return int(hour),overspill