print("Checking for Updates")
import Search, Main
import update_check as Update
SearchGit = "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/main/Search.py?token=AH5HRBE2OA7EC25VLN4QYQK7VMVA4"
MainGit = "https://raw.githubusercontent.com/LoafOrc/MicrosoftRewardsPlus/main/Main.py?token=AH5HRBG4JYZCJNCTQBYOOXK7VMV4S"

#Check for Updates (Search.py)
if Update.isUpToDate(Search.__file__, SearchGit) == False:
    print("Updating Search.py")
    Update.update(Search.__file__, SearchGit)

#Check for Updates (Main.py)
if Update.isUpToDate(Main.__file__, MainGit) == False:
    print("Updating Main.py")
    Update.update(Main.__file__, MainGit)

print("Done checking for Updates")