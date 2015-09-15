"""
Polish: 5

finds text
replaces it with other text

uses glob to select target files
"""

import glob
import fileinput

file_format = "*.*"
py_files = glob.glob(file_format)

old = ""
new = ""

for py_file in py_files:
    for line in fileinput.input(py_file, inplace = True):
        print(line.replace(old, new).rstrip())
