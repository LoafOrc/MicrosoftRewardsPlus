import time,os,subprocess,sys

def DependencyCheck(module):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    if (module in installed_packages) == False:
        os.system("pip install " + module)

#Check Updates
from update_check import checkForUpdates

def ReadSettings():
    file1 = open('settings.txt', 'r')
    Lines = file1.readlines()

    count = 0
    for line in Lines:
        if(line.startswith("#")):
            continue
        count += 1

    Settings = [1]*count
    count = 0
    for line in Lines:
        if(line.startswith("#")): 
            continue
        Settings[count] = line.strip()
        count += 1
    return Settings

Settings = ReadSettings()

if(Settings[5] != "none"):
    checkForUpdates(__file__, "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/" + Settings[5] + "/Main.py")

def KillTask(task):
    print("Subprocess: Killing " + task +".exe")
    time.sleep(int(Settings[3]))
    os.system("taskkill /f /im " + task + ".exe")

def OpenSettings(sub):
    print("Subprocess: Opening Settings")
    os.system("start ms-settings:" + sub)

def BingSearch(Query):
    return('https://www.bing.com/search?q=' + str(Query))