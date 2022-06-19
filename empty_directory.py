import os


def empty_directory(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            empty_directory(file_path)
            print(file_path + " is removed")
            os.rmdir(file_path)
        else:
            os.remove(file_path)
            print(file_path + " is removed")