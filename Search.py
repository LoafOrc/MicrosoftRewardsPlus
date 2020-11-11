#Check Updates

import subprocess, sys, os

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

if ('update_check' in installed_packages) == False:
    os.system("pip install update_check")

from update_check import checkForUpdates


import webbrowser as edge
import Main

checkForUpdates(__file__, "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/" + Main.ReadSettings()[5] + "/Search.py")

Main.OpenSettings(Main.ReadSettings()[4])
input("User: Please change your deafault browser to Microsoft Edge")


#Main Loop
Main.KillTask(Main.ReadSettings()[2])
for TabRound in range(0, int(Main.ReadSettings()[0]), 1):
    for searching in range(0,int(Main.ReadSettings()[1]),1):
        
        #Create a unique Search
        edge.open(Main.BingSearch((searching + 1) * (TabRound + 1)))
    Main.KillTask("msedge")
edge.open('https://account.microsoft.com/rewards/')

Main.OpenSettings(Main.ReadSettings()[4])
input("User: You may now set your default browser back")
