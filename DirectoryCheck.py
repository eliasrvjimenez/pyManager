import os


def exists(path:str):
    return os.path.exists(path)

def create_dir(path:str):
    if exists(path):
        pass
    else:
        os.mkdir(path)
        print("Folder %s created!" % path)

def get_home():
    return os.path.expanduser("~")

def get_settings():
    return get_home() + '/.pymanager/settings.json'
    