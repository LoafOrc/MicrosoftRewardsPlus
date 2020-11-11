import time,os

#Check Updates
from update_check import checkForUpdates

checkForUpdates(__file__, "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/main/Main.py")


def KillTask(task):
    print("Subprocess: Killing " + task +".exe")
    time.sleep(int(ReadSettings()[3]))
    os.system("taskkill /f /im " + task + ".exe")

def OpenSettings(sub):
    print("Subprocess: Opening Settings")
    os.system("start ms-settings:" + sub)

def BingSearch(Query):
    return('https://www.bing.com/search?q=' + str(Query))

def ReadSettings():
    file1 = open('settings.txt', 'r')
    Lines = file1.readlines()

    Settings = [1]*len(Lines)
    count = 0
    for line in Lines:
        if(line.startswith("#")): 
            continue
        Settings[count] = line.strip()
        count += 1
    return Settings