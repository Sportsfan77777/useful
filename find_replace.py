"""
Polish: 9

Example Usage:
(1) python find_replace.py
(2) python find_replace.py -f "replaceThis" -r "withThis"
(3) python find_replace.py -f "replaceThis" -r "withThis" --format "inTheseFiles"

*** If you use method (1), all of the defaults must be changed in the script ***
*** If you use method (2), the default file format must be changed in the script ***
    

Optional Arguments:
  -h, --help            displays help message and exits
  -f FIND               text to find
  -r REPLACE            text to replace
  --format=FILE_FORMAT  search files with this glob.glob format

Author's Notes:
At present, it is easiest to use this script in the same directory as the target files.
Though, this script may be used in other directories if the file format is properly specified.
"""

import glob
import fileinput
from optparse import OptionParser

####### DEFAULTS (an alternative to supplying these as arguments) #######

# (1,2) Replace Old Text 'default_old' with 'default_new'
default_old = ""
default_new = ""

# (3) Search these files (Example formats: "file.txt", "*.txt", "*.py", "*.*")
default_format = ""


def find_replace(old, new, file_format):
    """
    Parameters: old, new, file_format

    (1) Finds all files matching the wildcard 'file_format'
    (2) For each file, replace any occurence of 'old' with 'new'

    Returns: nothing
    """

    filenames = glob.glob(file_format)

    for fn in filenames:
        for line in fileinput.input(fn, inplace = True):
            print(line.replace(old, new).rstrip())


def new_option_parser():
    """ 
    Handles input

    Returns: OptionParser
    """
    parser = OptionParser()
    parser.add_option("-f", 
                      dest="find", default = None,
                      help="text to find")
    parser.add_option("-r", 
                      dest="replace", default = None,
                      help="text to replace")
    parser.add_option("--format", 
                      dest="file_format", default = None,
                      help="search files with this glob.glob format")
    return parser

######## MAIN ########
if __name__ == '__main__':
    parser = new_option_parser()
    options, args = parser.parse_args()

    ### Future Modification: also handle arguments without optionParser ###

    # Check for supplied arguments
    if options.find is None:
        options.find = default_old

    if options.replace is None:
        options.replace = default_new

    if options.file_format is None:
        options.file_format = default_format

    # Find + Replace
    find_replace(options.find, options.replace, options.file_format)


