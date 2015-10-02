import time
import os

print("Converting all iPython Notebooks to markdown text files")

def create_file(file_name):
    original_file_name = file_name
    file_name = "content/notebooks/"+file_name

    print("Converting "+file_name)

    # Get file modified time
    t = time.ctime(os.path.getmtime(file_name))
    file_name = file_name.replace('notebooks/', '').replace('ipynb', 'md')

    f = open(file_name, 'w')
    f.write("Title:{}\n".format(file_name.replace('content/', '').replace('.md', '')))
    f.write("Date:{}\n".format(t))
    f.write("\n\n")
    f.write("{% notebook "+original_file_name+" %}")
    f.close()

import os
for file in os.listdir("content/notebooks"):
    if file.endswith(".ipynb"):
        create_file(file)
