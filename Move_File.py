import os
import shutil
from unicodedata import name

from_dir="C:/Users/sunis"
to_dir="C:/Users/sunis/Desktop/Project C111/Document_files"
list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name,ext = os.path.splitext(file)
