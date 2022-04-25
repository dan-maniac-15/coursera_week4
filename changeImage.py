#! /usr/bin/python3
import subprocess
from subprocess import PIPE
import PIL
from PIL import Image

old_file_directory = "supplier-data/images/"
new_file_directory = "supplier-data/images/"

#get the list of file names under a directory
result = subprocess.run(["ls", old_file_directory], capture_output=True)

result_list = result.stdout.decode().split()

#execute to each file
for i in result_list:
    if i[len(i)-4:] == 'tiff':
        im = Image.open(old_file_directory + i)
        im.convert('RGB').resize((600,400)).save(new_file_directory + i[:-4] + 'jpeg', 'JPEG')