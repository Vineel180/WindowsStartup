from subprocess import run as openTerminal
from os import startfile as openTarget
from webbrowser import open as openSite

def openTerminalS(List):
    for i in List:
        openTerminal(i, shell=True)
def openTargetS(List):
    for i in List:
        openTarget(i)
def openSiteS(List):
    for i in List:
        openSite(i)

def openTerminalS_ifMatch(List, Match):
    for i in List:
        if i[0] == Match:
            openTerminal(i[1], shell=True)
def openTargetS_ifMatch(List, Match):
    for i in List:
        if i[0] == Match:
            openTarget(i[1])
def openSiteS_ifMatch(List, Match):
    for i in List:
        if i[0] == Match:
            openSite(i[1])

def openTerminalS_skipMatch(List):
    for i in List:
        openTerminal(i[1], shell=True)
def openTargetS_skipMatch(List):
    for i in List:
        openTarget(i[1])
def openSiteS_skipMatch(List):
    for i in List:
        openSite(i[1])

