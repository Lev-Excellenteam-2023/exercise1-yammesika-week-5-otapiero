import os


# function that gets a folder path and return a string of file names who starts with "deep" in the folder
def fun(path):
    # get all files in the path

    files = os.listdir(path)

    # filter the files who starts with "deep"

    files = [file for file in files if file.startswith("deep")]

    # return the files
    print(files)

    return files
#fun("C:\\Users\\ouriel\\source\\repos\\otapiero\\levExcelents\\Python\\Notebooks-master\\Notebooks-master\\week05\\images")
