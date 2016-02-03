#!/usr/bin/env python3
#
# Program:      copy2bin.py
# Version:      1.0
# Restrictions: Python3 only. Linux platform only.
#
# Objective:    A function for copying a python script to /usr/local/bin/.
#               The copied file is then set to be executable.
#               From a Linux bash prompt the python file will then launch.
#
#               copy2bin is also intended as a module that its "copy_to_bin"
#               function may be called from another python program. That other
#               program will then be to coped to /usr/local/bin/. In order to
#               import the function "copy_to_bin" from copy2bin.py module place
#               copy2bin.py in /usr/local/lib/python3.4/dist-packages/ 
#               This can be done with the command:
#               $ sudo python3 copy2bin.py copy2bin.py
#
# Recommend:    Place this file in /usr/local/bin/copy2bin with chmod +x
#               E.g. $ sudo python3 copy2bin.py copy2bin.py
#
# Author:       Ian Stewart
# Date:         2016-Jan-26
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation
#
# Python modules to be imported
import sys
import os
import shutil
import string
# Check Python is version 3. No interest in supporting Python2.
if int(sys.version[0]) < 3:
    print("Python Version Error: Run program using python3. "
          "\nExiting...")
    sys.exit()
#
HELP_INFO = """copy2bin
Usage: $ python3 copy2bin.py [FILE / OPTION]
Copy a python3 FILE to /usr/local/bin/, so it may be launched from bash.
Must be run with sudo permissions.

Arguments:
    [FILE]          Python3 file with shebang of #!/usr/bin/env python3
    -h  --help      Display this help information.

Example:
$ sudo python3 copy2bin.py my_program.py
To run my_program.py from bash prompt
$ myprogram

If copy2bin.py has been placed in /usr/local/bin/, then an example would be:
$ sudo copy2bin my_program.py
"""


def copy_to_bin(python_file, path="/usr/local/bin/"):
    """
    On a linux platform, copy a python file to /usr/local/bin/ so it may be
    launched with bash. Requires sudo permissions.
    E.g. /home/user/My_Program.py to /usr/local/bin/myprogram
    The file copied to /usr/local/bin/ is modified to have execute permissions.
    A check is made to ensure the shebang is #!/usr/bin/env python3
    Provide prompting of a new name, based on the python file name. E.g.
    If python program is 'My_Program.py' prompt with 'myprogram'
    """
    # Exit if python_file does not exist.
    if not os.path.isfile(python_file):
        print("The file {} does not exist.".format(python_file))
        sys.exit()

    # Exit if not linux. print(sys.platform) # linux
    if not sys.platform == "linux":
        print("This function is only supported on the Linux platform.")
        sys.exit()
    # Exit if user is not root
    user = os.getenv("SUDO_USER")
    if user is None:
        print("Using Copy to /usr/local/bin/ requires 'sudo' permission.")
        print("Please launch again, but with $ sudo...")
        sys.exit()
    # Check if the python file has a shebang of #!/usr/bin/env python3
    with open(python_file, 'r') as f:
        first_line = f.readline().rstrip()
        if not first_line == "#!/usr/bin/env python3":
            print("Shebang Error: Change '{}' in {} to:\n"
                  "#!/usr/bin/env python3"
                  .format(first_line, python_file))
            sys.exit()
    # Produce a prompt. Strip any path and strip .py. E.g. /user/File name.py
    prompt = os.path.basename(python_file)  # strip path -->File name.py
    prompt = prompt.lower()  # Lower case -->file name.py
    prompt = os.path.splitext(prompt)[0]  # Extension -->file name
    prompt = prompt.replace(" ", "")  # Remove spaces. -->filename
    prompt = prompt.replace("_", "")  # Remove any underscores
    response = input("Provide a name for your python program [{}]: "
                     .format(prompt))
    if response == "":
        response = prompt
    else:
        # Clean up the User input response if necessary.
        response = response.strip(' \t\n\r')  # Strip whitespace
        response = response.replace(" ", "")  # Remove any spaces - concatinate
        response = response.replace("\t", "")  # Remove any tabs between words
        response = response.replace("_", "")  # Remove any underscores
    # Check if new program name is suitable
    allowed = set("{}{}{}{}".format(string.ascii_lowercase, string.digits,
                                    '.', '-'))
    if not set(response) <= allowed:
        print("A program name of {} is not permitted.".format(response))
        print("The new name should only use characters a to z, 0 to 9, -, .")
        print("Exiting...")
        sys.exit()
    # Attempt to copy the file to /usr/local/bin/ and set it to execute
    path_file = "{}{}".format(path, response)
    try:
        shutil.copy2(python_file, path_file)
    except shutil.SameFileError:
        print("SameFileError: Files source and destination are the same.")
        sys.exit()
    status = os.stat(path_file)
    os.chmod(path_file, status.st_mode | 0o111)  # Allow execution. chmod +x
    # Finished message...
    print("At the command line prompt type {} to execute the program."
          .format(response))
    return


if __name__ == "__main__":
    """
    copy2bin.py expects a python program as sys.argv[1].
    E.g. $ sudo copy2bin.py my_program.py
    If sys.argv[1] is --help or -h print the help information.
    Otherwise, pass sys.argv[1] in the copy_to_bin() function.
    """
    if len(sys.argv) > 1:
        argument_1 = sys.argv[1]
    else:
        print("copy2bin filename not provided. Exiting...")
        sys.exit()

    if argument_1 == "-h" or argument_1 == "--help":
        print(HELP_INFO)
        sys.exit()

    # $ sudo copy2bin myprog.py
    # Assume sys.argv[1] is python file to copy to /usr/local/bin/
    if not argument_1 == "copy2bin.py":
        copy_to_bin(argument_1)
        sys.exit()
    else:
        # Special case where copy2bin is copying itself. E.g.
        # sudo python3 copy2bin.py copy2bin.py
        #
        # Initially place copy2bin.py into /usr/local/bin/copy2bin
        copy_to_bin(argument_1)

        # Next place copy2bin.py into /usr/local/lib/python3.4/dist-packages/
        path_file = "/usr/local/lib/python3.4/dist-packages/"
        path_file_name = "{}{}".format(path_file, argument_1)
        try:
            shutil.copy2(argument_1, path_file)
        except shutil.SameFileError:
            print("SameFileError: Files source and destination are the same.")
            sys.exit()

'''
Concepts on naming - from googling:

POSIX defines: 3.231
Name a word consisting solely of underscores, digits, and alphabetics from
the portable character set. The first character of a name is not a digit.

Shell and Tools standard doesn't define the lexical convention for variable
names, however a cursory look at the source reveals it uses something similar
to [a-zA-Z_]+[a-zA-Z0-9_]*

Linux characters that work
_~!@#$%^.,[]+

Characters that dont work...
 ><'"|=()`.

Opted for:
string.ascii_lowercase, string.digits, '.', '-'

===

To call from another program. Embed the following code in the other program...

if __name__ == "__main__":
    """Check for command line argument. Provide copying to bin."""
    print(TITLE_2)
    if len(sys.argv) > 1:
        argument_1 = sys.argv[1]
    else:
        argument_1 = None

    if argument_1 == "-h" or argument_1 == "--help":
        print("TODO: Write help info about this program. Include --copy2bin")
        sys.exit()

    if argument_1 == "--copy2bin":
        try:
            from copy2bin import copy_to_bin
            copy_to_bin(sys.argv[0])
            sys.exit()
        except ImportError:
            print("ImportError: from copy2bin import copy_to_bin")
            print("Place copy2bin.py into "
                  "/usr/local/lib/python3.4/dist-packages/")
            sys.exit()
    #else:
    # Run the program normally...

'''
