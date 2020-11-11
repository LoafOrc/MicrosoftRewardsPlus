#Check Updates
import Update
print("Libraries: Importing")

import webbrowser as edge
import Main
    
print("Libraries: Successfully Imported")
print("Checking For Updates")

Main.OpenSettings(Main.ReadSettings()[4])
input("User: Please change your deafault browser to Microsoft Edge")


#Main Loop
Main.KillTask(Main.ReadSettings()[2])
for TabRound in range(0, int(Main.ReadSettings()[0]), 1):
    for searching in range(0,int(Main.ReadSettings()[1]),1):
        
        print("Tab: Opening, " + str(searching * (TabRound + 1)))
        #Create a unique Search
        edge.open(Main.BingSearch((searching + 1) * (TabRound + 1)))
    Main.KillTask("msedge")
edge.open('https://account.microsoft.com/rewards/')

Main.OpenSettings(Main.ReadSettings()[4])
input("User: You may now set your default browser back")