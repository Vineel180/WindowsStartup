import Settings.Settings as s

print('Windows-Startup-Auto was unable to connect to internet.')
userInput = input('Press "1 + Enter" to reset the retry-counter. Press "Enter" to stop the program.')

with open(s.internetRetryStateTxt_filePath, "wt") as file:
    file.write(userInput)
