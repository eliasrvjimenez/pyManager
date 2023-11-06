from os.path import expanduser
import os
import json
import DirectoryCheck as check


def change_curr_settings (settings:dict): 
    """Changes Current Settings for pyManager"""

def setup_new (settings:dict):
    home = expanduser("~")
    downloads_path = home + os.sep + "Downloads"
        
    is_setting_up = True
    while(is_setting_up):
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
                    print("Please input a valid path")
                else:
                    settings["fileOrganizer"]["Downloads"] = new_downloads
                no_answer1 = False
            else:
                print("please type Y or N")
        no_answer2 = True
        while(no_answer2):
            answer2 = (input("""Would you like to have organized downloads:\n
                                1. Stay in the Downloads folder?\n
                                2. Go in a separate folders?\n"""))
            if answer2 == '2':
                pass

# def setup_separated


if __name__ == "__main__":
    f = open(check.get_settings(), 'r')
    settings = json.load(f)

    print("Welcome to pyManager setup, let's begin")
    
    if settings["hasRunSetup"] == False:
        print("Running First-Time Setup...")
    else:
        print("ran setup before, cancelling")
    

   
    

    

    # if settings["hasRunSetup"] == True:
    #     answer0 = input("""Looks like you've already set up pyManager, would you like to: \n
    #                     1. Run a fresh setup?\n
    #                     2. Change some settings?\n """)
    #     if answer0 == '2':
    #         pass
        




