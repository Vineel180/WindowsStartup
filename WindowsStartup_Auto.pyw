import Settings.Settings as s
from datetime import datetime
from time import time as timeTime

def getDateTimeWeekdayNow():
    now = datetime.now()
    date = now.strftime("Y%d%m")
    time = now.strftime("%H%M%S")
    weekday = now.weekday() # sunday == 6
    return date, time, weekday, now

def readFile(filePath):
    with open(filePath, "rt") as file:
        return file.read()

def runRepeatersQ():
    timeSecs = timeTime()
    lastTimeSecs = float(readFile(s.lastTimeTxt_filePath))
    if timeSecs - lastTimeSecs > s.rerunRepeatersAfterTime:
        return True
    else:
        return False

if __name__ == "__main__":
    date, time, weekday, now = getDateTimeWeekdayNow()
    if runRepeatersQ():
        ...

#    if int(time) > int(s.startAppAfterTime):
#        lastDate = readFile(s.lastDateTxt_filePath)
