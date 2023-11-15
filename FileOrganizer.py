##################
# Created by Elias Vera-Jimenez 
##################

import os
import shutil
import ntpath
import send2trash
import json
import DirectoryCheck as check

# settings.json contains all of the file_organizer settings for the client, created using setup.py
f = open(check.get_settings())
settings = json.load(f)
folders = settings["fileOrganizer"] 
# a list of all the directories to move files to. 

def is_sort_folder(path:str):
    for file_type, folder_path in folders.items():
        if path == folder_path: return True
    return False

def file_sort (file_path:str, folder:str) :
    """ Sorts the files passed to it by file_type_check,
    takes a string representing the path to the file being sorted,
    and a string representing a path to the folder where the file will
    be moved."""
    new_path = folder + "/" + ntpath.basename(file_path)
    
    try:
        if os.path.exists(new_path):
            send2trash.send2trash(file_path)
            return "%s Moved to Trash" % file_path
        else:
            shutil.move(file_path, folder)
            return  "%s Moved to %s " % (file_path, folder)
    except OSError:
        exit("Did not move files, path %s does not exist. \n Did you set up settings.txt correctly?" % folder)
        



def file_type_check (file : str):
    """ Checks the extension at the end of a file and calls
    file_sort, passing it the file's path and the folder associated with the
    file's extension."""
    if file == folders["Downloads"] + '/.DS_Store':
        return (0,)      
    if is_sort_folder(file):
        return (0,"")
    file_ext = os.path.splitext(file)[-1]
    if file_ext == '.dmg':
        return 1, file_sort(file, folders["InstallerFiles"])
    elif file_ext == '.jpg' or file_ext == '.png':
        return 1, file_sort(file, folders["DownloadedPics"])
    elif file_ext == '.pdf':
        return 1, file_sort(file, folders["DownloadedDocs"])  
    elif file_ext == '.zip':
        return 1, file_sort(file, folders["DownloadedZips"])
    elif file_ext == '.xlsx':
        return 1, file_sort(file, folders["DownloadedSheets"])
    else:
        return 1, file_sort(file, folders["DownloadedMisc"])

def run_sort ():
    """Used to sort the downloads into their respective folders. Takes no arguments."""
    dir = folders["Downloads"]
    if len(os.listdir(dir)) == 0:
        print("No files to sort, Directory %s empty or already sorted." % dir)
    num_sorted = 0
    for file in os.listdir(dir):
        checked = file_type_check(dir + "/" + file)
        if checked[0]: print("*****************\n" + checked[1] + "*****************\n")
        num_sorted = num_sorted + checked[0]
    return num_sorted


if __name__ == "__main__":
    valid_answer = False
    while not valid_answer:
        run = input("Do you want to run FileOrganizer? [Y/N]\n")
        if run == "Y" :
            sorted_count = run_sort()
            if sorted_count > 0: print("Number of Sorted files: " + str(sorted_count))
            else: print("No files to sort, Directory %s empty or already sorted." % dir)
            valid_answer = True
        elif run == "N":
            valid_answer = True
        else:
            print("Please type Y or N.")