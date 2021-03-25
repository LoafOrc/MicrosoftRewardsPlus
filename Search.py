#Check Updates



import webbrowser as edge
import Main
Main.DependencyCheck('update_check')

from update_check import checkForUpdates
if(Main.Settings[5] != "none"):
    checkForUpdates(__file__, "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/" + Main.Settings[5] + "/Search.py")

Main.OpenSettings(Main.Settings[4])
input("User: Please change your default browser to Microsoft Edge")


#Main Loop
Main.KillTask(Main.Settings[2])
for TabRound in range(0, int(Main.Settings[0]), 1):
    for searching in range(0,int(Main.Settings[1]),1):
        
        #Create a unique Search
        edge.open(Main.BingSearch(searching + TabRound*int(Main.Settings[1])))
    Main.KillTask("msedge")
edge.open('https://account.microsoft.com/rewards/')

Main.OpenSettings(Main.Settings[4])
input("User: You may now set your default browser back")
