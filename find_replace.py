"""
Polish: 5

finds text
replaces it with other text

uses glob to select target files
"""

import glob
import fileinput

py_files = glob.glob("runPlanet*.py")

s = ""

for py_file in py_files:
    for line in fileinput.input(py_file, inplace = True):
        print(line.replace('fine', 
                      'extend').rstrip())
