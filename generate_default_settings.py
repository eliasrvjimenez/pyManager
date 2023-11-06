# Created by Elias Vera-Jimenez
import DirectoryCheck as check
import json

def new_settings(path):
    if check.exists(path):
        has_not_answered = True
        while(has_not_answered):
            reset_settings = input("settings.json already exists, reset settings? (Y/N) ")
            if reset_settings == ("N" or "n"):
                has_not_answered = False
                pass
            elif reset_settings == ("Y" or "y"):
                with open(path, 'w') as outfile:
                    json_object = json.dumps(blank_settings, indent = 4)
                    outfile.write(json_object)
                has_not_answered = False
                print("Settings Reset")
                pass
            else:
                print("please type Y or N") 
    else:
        check.create_dir(dir + '/.pymanager/')
        with open(path, 'w') as outfile:
            json_object = json.dumps(blank_settings, indent = 4)
            outfile.write(json_object)
        
if __name__ == "__main__":
    blank_settings:dict = {
        "hasRunSetup" : False, 
        "fileOrganizer" : {
            "downloadsAreSeparate":False,
            "Downloads": "",
            "SortedDownloads" : "",
            "InstallerFiles": "",
            "DownloadedPics": "",
            "DownloadedZips": "",
            "DownloadedDocs": "",
            "DownloadedSheets": "",
            "DownloadedMisc": ""
        }
    }
    settings_path = check.get_settings()
    new_settings(settings_path)
