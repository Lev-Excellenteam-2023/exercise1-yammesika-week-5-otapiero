import os


# function that gets a folder path and return a string of file names who starts with "deep" in the folder
def fun(path):
    # get all files in the path

    files = get_files_in_folder(path)

    # filter the files who starts with "deep"

    files = [file for file in files if file.startswith("deep")]

    # return the files
    print(files)

    return files
    
     
def get_files_in_folder(path):
    return os.listdir(path)
    
    
 def main():
    fun("C:\\Users\\ouriel\\source\\repos\\otapiero\\levExcelents\\Python\\Notebooks-master\\Notebooks-master\\week05\\images")
    
if __name__=="__main__":
    main()
