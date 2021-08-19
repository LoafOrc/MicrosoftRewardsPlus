#Check Updates



import webbrowser as edge
import Main
import os
Main.DependencyCheck('update_check')

from update_check import checkForUpdates
if(Main.Settings[5] != "none"):
    checkForUpdates(__file__, "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/" + Main.Settings[5] + "/Search.py")

#Main Loop
Main.KillTask(Main.Settings[2])
for TabRound in range(0, int(Main.Settings[0]), 1):
    for searching in range(0,int(Main.Settings[1]),1):
        
        #Create a unique Search
        query = Main.BingSearch(searching + TabRound*int(Main.Settings[1]))
        os.system("start msedge " + query)
    Main.KillTask("msedge")
os.system("start msedge https://account.microsoft.com/rewards/")