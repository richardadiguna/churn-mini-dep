import os
import glob


def create_dir(root_dir, directories):
    try:
        for directory in directories:
            path = os.path.join(root_dir, directory)
            if not os.path.isdir(path):
                os.makedirs(path)
        return
    except Exception as err:
        print("Creating driectories error: {0}".format(err))


def get_latest_file(dir_path):
    path = os.path.join(dir_path, '*')
    files = glob.glob(path)
    latest_file = max(files, key=os.path.getctime)
    return latest_file
