import os
import re

def rename_chapters(folder_path):
    # Loop through all files in the specified folder path
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            # Extract the chapter number and title from the HTML file
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = f.read()
                title = re.findall("<title>.*?Chapter (\d+): (.*?)</title>", content, re.DOTALL)
                if len(title) > 0:
                    chapter_number = title[0][0].zfill(3)
                    chapter_title = title[0][1]
                else:
                    continue
            # Create the new file name using the chapter number and title
            new_filename = chapter_number +" "+ chapter_title.replace(":", "") + ".html"
            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

#rename_chapters("C:\\Users\\ouriel\\source\\repos\\otapiero\\levExcelents\\Python\\Notebooks-master\\Notebooks-master\\week05\\resources\\potter - Copy")
