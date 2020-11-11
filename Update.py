print("Checking for Updates")
import update_check as Update
SearchGit = "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/main/Search.py"
MainGit = "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/main/Main.py"

def CheckForUpdates():
    print("Checking for Updates")
    #Check for Updates (Search.py)
    if Update.isUpToDate("\\.\\Search.py", SearchGit) == False:
        print("Updating Search.py")
        Update.update("\\.\\Search.py", SearchGit)

    #Check for Updates (Main.py)
    if Update.isUpToDate("\\.\\Main.py", MainGit) == False:
        print("Updating Main.py")
        Update.update("\\.\\Main.py", MainGit)

    print("Done checking for Updates")
