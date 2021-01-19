import os

def get_path(path):
    path_ = os.path.join(os.getcwd(), path)
    if not os.path.isfile(path_):
        raise Exception("Not a valid path")
    return path_

def get_template(path):
    path_=get_path(path)
    return open(path_).read()
