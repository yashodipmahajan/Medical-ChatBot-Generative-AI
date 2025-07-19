# to  make an project structure... you can also make the files by hand.. 
# but if more files are there then you can use this logic to make the files...

import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath= Path(filepath)

    # see while creating file we are using forward slash and but in windows os
    #  they use backward slash and in linux they use forward slash .. so to adjust accordingly we are using this..
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) :
        with open(filepath,"w"):
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exist")