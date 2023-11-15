from os.path import expanduser
import os
import json
import DirectoryCheck as check

def setup_dir(extension:str) -> str:
    path = input("Where would you like %s to be stored?\n" % (extension))
    set_path = ""
    if not (path[0] == "~" or path[0:len(check.get_home())] == check.get_home()):
        print("Path needs to be in somewhere in the main directory.")
        set_path = setup_dir(extension)
    else:
        try:
            set_path = check.create_dir(path)
            print("%s will be stored in %s" % (extension, set_path))
        except OSError:
            print("Please input a valid directory path")
            set_path = setup_dir(extension)
            pass
    return set_path

def change_curr_settings (settings:dict): 
    """Changes Current Settings for pyManager"""
    for setting in settings["fileOrganizer"]:
        if setting == "downloadsAreSeparate":continue
        if setting == "Downloads":continue
        if setting == "SortedDownloads":continue
        valid_answer = False
        while not valid_answer:
            print (" %s is currently located at %s " % (setting, settings["fileOrganizer"][setting]))
            answer1 = input("Do you want to change it's location? [Y/N]\n")
            if answer1 == 'Y':
                new_setting_path = setup_dir(setting)
                settings["fileOrganizer"][setting] = new_setting_path
                valid_answer = True
            elif answer1 == "N": valid_answer = True
            else: print("please type Y or N")
    return settings



def setup_new (settings:dict):
    """Runs Default Setup Procedures, 3 main options: \n
        - Express Setup (Within Downloads): Creates organization folders using the default names created, within the Downloads folder.\n
        - Express Setup (Outside Downloads): User chooses what to call the new sorted downloads folder in home directory, and the default organization folder names are placed in that folder. \n
        - Custom Setup: User chooses where all of the individual sorted downloads go, will create new directories for the user if they have not yet been made. requires user to input the direct path.\n
        """

    downloads_path = check.get_home() + "/Downloads"
        
    #question1
    no_answer1 = True
    while(no_answer1):
        answer1 = (input("Your Downloads folder is at %s, is this correct? (Y/N)\n" % downloads_path)) 
        if answer1 == ("Y" or "y"):
            settings["fileOrganizer"]["Downloads"] = downloads_path
            print("answered yes")
            no_answer1 = False
        elif answer1 == ("N" or "n"):
            new_downloads = input("What is the path to your Downloads folder? \n")
            if check.exists(new_downloads):
                settings["fileOrganizer"]["Downloads"] = new_downloads
                downloads_path = new_downloads
                no_answer1 = False
            else:
                print("please input valid path.")
            
        else:
            print("please type Y or N")
    #end question1

    #question2
    no_answer2 = True
    while(no_answer2):
        answer2 = (input("""What setup type would you like:\n
        - 1. Express Setup (Within Downloads): Default organization folders will be created within Downloads, and kept there. all organized files will be sorted into this folder. \n
        - 2. Express Setup (Outside Downloads): Organization Folders will be created outside of downloads, \n
        - 3. Custom Setup: You choose where all of the separate file types get organized by providing your chosen paths, will create new directories if necessary. \n
        1, 2, or 3? -> 
        """))
        if answer2 == '1':
            dirs = {
                "InstallerFiles": downloads_path+"/Installer Files",
                "DownloadedPics": downloads_path+"/Downloaded Pictures",
                "DownloadedZips": downloads_path+"/Downloaded Zips",
                "DownloadedDocs": downloads_path+"/Downloaded Documents",
                "DownloadedMisc": downloads_path+"/Misc",
                "DownloadedSheets": downloads_path+"/Downloaded Sheets"
            }

            for file_type in settings["fileOrganizer"]:
                if file_type == "Downloads" or file_type == "SortedDownloads" or file_type == "downloadsAreSeparate":
                    continue
                else:
                    path = check.create_dir(dirs[file_type])
                    print("%s will be stored in %s" % (file_type, path))
                    settings["fileOrganizer"][file_type] = path
                
            no_answer2 = False
        elif answer2 == '2':
            not_valid_path = True
            sorted_downloads = ""
            while(not_valid_path):
                sorted_downloads = input("Where do you want the sorted files to go? (type in the path to the folder, will create new folder if needed)\n")
                if not (sorted_downloads[0] == "~" or sorted_downloads[0:len(check.get_home())] == check.get_home()):
                    print("Path needs to be in somewhere in the main directory.") 
                else:
                    if sorted_downloads[0] == "~": sorted_downloads = check.get_home()+sorted_downloads[1:]
                    sorted_downloads = check.create_dir(sorted_downloads)
                    not_valid_path = False

            settings["fileOrganizer"]["downloadsAreSeparate"] = True
            settings["fileOrganizer"]["SortedDownloads"] = sorted_downloads
            
            dirs = {
                "InstallerFiles": sorted_downloads + "/Installer Files",
                "DownloadedPics": sorted_downloads + "/Downloaded Pictures",
                "DownloadedZips": sorted_downloads + "/Downloaded Zips",
                "DownloadedDocs": sorted_downloads + "/Downloaded Documents",
                "DownloadedMisc": sorted_downloads + "/Misc",
                "DownloadedSheets": sorted_downloads + "/Downloaded Sheets"
            }

            for file_type in settings["fileOrganizer"]:
                if file_type == "Downloads" or file_type == "SortedDownloads" or file_type == "downloadsAreSeparate":
                    continue
                else:
                    path = check.create_dir(dirs[file_type])
                    print("%s will be stored in %s" % (file_type, path))
                    settings["fileOrganizer"][file_type] = path
            no_answer2 = False
        elif answer2 == '3':
            settings["fileOrganizer"]["downloadsAreSeparate"] = True
            settings["fileOrganizer"]["SortedDownloads"] = downloads_path
            for file_type in settings["fileOrganizer"]:
                if file_type == "Downloads" or file_type == "SortedDownloads" or file_type == "downloadsAreSeparate":
                    continue
                else:
                    path = setup_dir(file_type)
                    settings["fileOrganizer"][file_type] = path
            no_answer2 = False
        else:
            print("Please input a valid option")
    #end question2
    settings["hasRunSetup"] = True
    return settings
        
            
                

            


# def setup_separated


if __name__ == "__main__":
    f = open(check.get_settings(), 'r')
    settings = json.load(f)

    print("Welcome to pyManager setup, let's begin")
    
    if settings["hasRunSetup"] == False:
        print("Running First-Time Setup...")
        settings = setup_new(settings)
    else:
        print("ran setup before, changing settings...")
        settings = change_curr_settings(settings)
    with open(check.get_settings(), 'w') as outfile:
            json_object = json.dumps(settings, indent = 4)
            outfile.write(json_object)
        




