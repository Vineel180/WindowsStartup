import Settings.Settings as s
import Settings.LibraryController as c
from datetime import datetime
from time import time as timeTime
import socket
from time import sleep
from subprocess import Popen as subprocessPopen
from sys import exit as sysExit

def getDateTimeWeekdayNow():
    now = datetime.now()
    date = now.strftime("%Y%d%m")
    time = now.strftime("%H%M%S")
    weekday = now.weekday() # sunday == 6
    return date, time, weekday, now
def runRepeatersQ():
    timeSecs = timeTime()
    lastTimeSecs = float(readFile(s.lastTimeTxt_filePath))
    if timeSecs - lastTimeSecs > s.rerunRepeatersAfterTimeInterval:
        writeFile(s.lastTimeTxt_filePath, timeSecs)
        return True
    else:
        return False

def readFile(filePath):
    with open(filePath, "rt") as file:
        return file.read()
def writeFile(filePath, dataToWrite):
    """converts dataToWrite into string"""
    with open(filePath, "wt") as file:
        file.write(str(dataToWrite))

def checkInternet():
    for i in s.dnsServerS:
        try:
            socket.create_connection(i, timeout=s.timeoutTimeLimit)
            return True
        except (socket.timeout, socket.gaierror):
            continue
    return False
def waitForInternet():
    i = 0
    while not checkInternet():
        i += 1
        if i >= (s.attemptXCycles_beforeForcedExit):
            subprocessPopen(["start", "cmd", "/k", s.popupDialogueBox_filePath], shell=True)
            if readFile(s.internetRetryStateTxt_filePath) == "1":
                writeFile(s.internetRetryStateTxt_filePath, "0")
                i=0
            else:
                sysExit()
        sleep(s.retryEveryXSecs)
    return True

def main():
    c.runDaily(True)
    c.runWeekly(True)
    c.runMonthly(True)
    c.runQuarterly(True)
    c.runYearly(True)
    c.runDaily(False)
    c.runWeekly(False)
    c.runMonthly(False)
    c.runQuarterly(False)
    c.runYearly(False)

if __name__ == "__main__":
    date, time, weekday, now = getDateTimeWeekdayNow()
    runRepeatersQ_state = runRepeatersQ()
    # repeater 1/2
    if runRepeatersQ_state:
        c.runRepeaters(True)
    # main 1/1
    if int(time) > int(s.startAppAfterTime):
        lastDate = readFile(s.lastDateTxt_filePath)
        if lastDate != date:
            if waitForInternet():
                writeFile(s.lastDateTxt_filePath, date)
                main()
    # repeater 2/2
    if runRepeatersQ_state:
        c.runRepeaters(False)
