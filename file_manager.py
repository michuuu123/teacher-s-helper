import shutil
import os

sourcePath = r'source_files\s1'

destinationPath = r'dest_files\s1'

try:
    shutil.move(sourcePath, destinationPath)
except:
    os.mkdir(os.path.normpath(os.path.join(destinationPath, os.path.pardir)))
    shutil.move(sourcePath, destinationPath)