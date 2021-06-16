import sys
import os
from PIL import Image 


parent_dir = "C:\Dipanker\python learning\ztmLearning\JPGtoPNGConverter.py\\" 
# Gets 1st and 2nd argument which respresents the getter folder and the destination folder 
get_folder = sys.argv[1]
dest_folder = sys.argv[2]

if not os.path.isdir(dest_folder):  # checks if the destination folder doesn't exists
    os.mkdir(dest_folder)  # makes a new directory 

# Loops through the getter folder and searches image files
for filename in os.listdir(get_folder):  
    if filename.endswith('.jpg'):  # checks if the file is an image
        with Image.open(get_folder + filename) as img:
            pre, ext = os.path.splitext(filename)  # splits the filename and it's extension
            ext = '.png'  # changing the extension to png
            img.save(dest_folder + pre + ext, 'png')  # saves the file in a folder with path 'dest_folder' and name 'pre' and extension 'ext'
