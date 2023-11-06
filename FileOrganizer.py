##################
# Created by Elias Vera-Jimenez 
##################

import os
import shutil
import ntpath
import send2trash
import json

# settings.json contains all of the file_organizer settings for the client, created using setup.py
f = open('settings.json')
settings = json.load(f)
folders = settings["file_organizer"] 
# a list of all the directories to move files to. 



class FileOrganizer():
    """Class for organizing Files using a given path\n
        Methods:\n\
        - file_sort: Sorts the files passed to it by file_type_check,
        takes a string representing the path to the file being sorted,
        and a string representing a path to the folder where the file will
        be moved.\n
        - file_type_check: Checks the extension at the end of a file and calls
        file_sort, passing it the file's path and the folder associated with the
        file's extension."""


    def file_sort (self, file_path:str, folder:str) :
        """ Sorts the files passed to it by file_type_check,
        takes a string representing the path to the file being sorted,
        and a string representing a path to the folder where the file will
        be moved."""
        new_path = folder + "/" + ntpath.basename(file_path)
        
        try:
            if os.path.exists(new_path):
                send2trash.send2trash(file_path)
                print("******************")
                print("%s Moved to Trash" % file_path)
                print("******************")
            else:
                shutil.move(file_path, folder)
                print("******************")
                print("%s Moved to %s " % (file_path, folder))
                print("******************")
        except OSError:
            exit("Did not move files, path %s does not exist. \n Did you set up settings.txt correctly?" % folder)
            



    def file_type_check (self, file : str):
        """ Checks the extension at the end of a file and calls
        file_sort, passing it the file's path and the folder associated with the
        file's extension."""

        if file == folders["Downloads"] + '/.DS_Store':
            return 0        
        file_ext = os.path.splitext(file)[-1]
        if file_ext == '.dmg':
            self.file_sort(file, folders["InstallerFiles"])
        elif file_ext == '.jpg' or file_ext == '.png':
            self.file_sort(file, folders["DownloadedPics"])
        elif file_ext == '.pdf':
            self.file_sort(file, folders["DownloadedDocs"])  
        elif file_ext == '.zip':
            self.file_sort(file, folders["DownloadedZips"])
        elif file_ext == '.xlsx':
            self.file_sort(file, folders["DownloadedSheets"])
        else:
            self.file_sort(file, folders["DownloadedMisc"])
        return 1
    
    def run_sort (self):
        """Used to sort the downloads into their respective folders. Takes no arguments."""
        dir = folders["Downloads"]
        if len(os.listdir(dir)) == 0:
            print("No files to sort, Directory %s empty." % dir)
        num_sorted = 0
        for file in os.listdir(dir):
            num_sorted = num_sorted + self.file_type_check(dir + "/" + file)
        if num_sorted > 0 : print("Number of Sorted files: " + str(num_sorted))
        else: print("No files to sort, Directory %s empty." % dir)
        


if __name__ == "__main__":
    organize = FileOrganizer()
    organize.run_sort()