import os

path = "empty_folder"

try:
    # os.remove(path)
    os.remove(path)
except FileNotFoundError:
    print("That was not found!")
except IsADirectoryError:
    print("This is a directory!")
