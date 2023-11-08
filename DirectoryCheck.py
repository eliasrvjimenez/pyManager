import os


def exists(path:str) -> bool:
    if path[0] == '~': path = get_home() + path[1:]
    return os.path.exists(path)

def create_dir(path:str) -> str:
    if path[0] == '~': path = get_home() + path[1:]
    if exists(path):
        return path
        pass
    else:
        os.mkdir(path)
        print("Folder %s created!" % path)
        return path

def get_home() -> str:
    return os.path.expanduser("~")

def get_settings() -> str:
    return get_home() + '/.pymanager/settings.json'
    