#!/usr/bin/env python3
import requests
import subprocess
from subprocess import PIPE

# This example shows how a file can be uploaded using
# The Python Requests module

old_file_directory = "supplier-data/images/"

#get the list of file names under a directory
result = subprocess.run(["ls", old_file_directory], capture_output=True)

result_list = result.stdout.decode().split()

#execute to each file
for i in result_list:
    if i[len(i)-4:] == 'jpeg':
        url = "http://localhost/upload/"
        with open(old_file_directory + i, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
