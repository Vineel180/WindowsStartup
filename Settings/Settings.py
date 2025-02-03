# startup conditions
startAppAfterTime = "040000" # HHMMSS
rerunRepeatersAfterTimeInterval = 3600 # seconds

# checking for internet connection
"""
    (), # format == ("dns", port),
"""
dnsServerS = [
    ("8.8.8.8", 53), # google
    ("1.1.1.1", 53), # cloudflare
]
timeoutTimeLimit = 5 # seconds
retryEveryXSecs = 5 # seconds
attemptXCycles_beforeForcedExit = 60
popupDialogueBox_filePath = r"D:\Code\ProgramFiles\WindowsStartup\AppData\lastTime\popup.py"
internetRetryStateTxt_filePath = r"D:\Code\ProgramFiles\WindowsStartup\AppData\lastTime\internetRetryState.txt"

# file paths
lastDateTxt_filePath = r"D:\Code\ProgramFiles\WindowsStartup\AppData\lastDate.txt"
lastTimeTxt_filePath = r"D:\Code\ProgramFiles\WindowsStartup\AppData\lastTime.txt"
