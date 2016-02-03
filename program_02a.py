#!/usr/bin/env python3
#
# Program:      program_02a.py
#
# Objective:    GUI application template using buttons, labels and frames
#               Use the program_01c.py and introduce the ttk.Frame
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Feb-01
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation.
# 2. #*** indicates a change from previous program.
#
# Python modules to be imported. Plus checking
import sys
import os

# Check Python is version 3
if int(sys.version[0]) < 3:
    print("Python Version Error: Run program using python3 to support "
          "tkinter.\nExiting...")
    sys.exit()
# Import tkinter and ttk modules
try:
    from tkinter import *
except ImportError as e:
    print("Import Error: tkinter module for python3 is not available.")
    print("To install tikinter: $ sudo apt-get install python3-tk")
    sys.exit()
try:
    from tkinter import ttk
except ImportError as e:
    print("Import Error: tkinter.ttk module is not available.")
    print("To install tikinter: $ sudo apt-get install python3-tk")
    sys.exit()

# Define Constants:
PROGRAM = "program_02a.py"
VERSION = "1.0"
TITLE_1 = "GUI Application. {} {}".format(PROGRAM, VERSION)
TITLE_2 = "Launching tkinter/ttk application. {} {}".format(PROGRAM, VERSION)
INFO_1 = "Program to highlight ttk.Frame."
INFO_2 = "The command line argument was "
BUTTON_1_TEXT = "Increment"
BUTTON_2_TEXT = "Decrement"
BUTTON_3_TEXT = "Close"

# Define Variables:
argument_1 = 0  # For command line first argument (sys.argv[1]).

# Main GUI application


class GUI_Application():

    def __init__(self, master, argument):
        """Setup the style, widgets and initial appearance on launching"""
        self.master = master
        master.title(TITLE_1)

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()

        # Change a root style to modify all widgets.
        self.style.configure('.', font=('FreeSans', 12))

        # Create a Blue style for the label. Use when value 0
        self.style.configure('blue.TLabel', foreground='white',
                             background='#0000ff', font=('FreeSans', 16),
                             padding=10)
        # Create a Green style for the label. Use when value is minus.
        self.style.configure('green.TLabel', foreground='black',
                             background='#00ff00', font=('FreeSans', 16),
                             padding=10)
        # Create a Red style for the label. Use when value plus.
        self.style.configure('red.TLabel', foreground='white',
                             background='#ff0000', font=('FreeSans', 16),
                             borderwidth=10)
        self.style.configure('small.TLabel', font=('FreeSans', 10))
        # Create a Frame style
        self.style.configure('cyan.TFrame', borderwidth=5, relief="ridge",
                             background='#00ffff')

        # ===== Create Widgets =====
        # Create Frames #***
        # Frame1. Relief = "sunken" "flat" "groove" "ridge" "raised"
        self.frame_1 = ttk.Frame(master, style='cyan.TFrame',
                                 padding="5 5 5 5")

        # Frame2
        self.frame_2 = ttk.Frame(master, padding="10 10 10 10", borderwidth=5,
                                 relief="ridge")
        # Frame3
        self.frame_3 = ttk.Frame(master, padding="10 10 10 10", borderwidth=5,
                                 relief="ridge")
        # Frame4
        self.frame_4 = ttk.Frame(master, padding="10 10 10 10", borderwidth=5,
                                 relief="groove")

        # Create Labels:
        # label_1 - Main label to display the status of the switches
        self.label_1 = ttk.Label(self.frame_1, text="")
        # Add label_1 into frame_1
        self.label_1.grid(row=0, column=0)  # , padx=5, pady=5) #, sticky=W)

        # label_2 - Program description
        self.label_2 = ttk.Label(self.frame_4, text=INFO_1)
        # label_3 - State the argument if one was passed.
        self.label_3 = ttk.Label(self.frame_4,
                                 text=('{} "{}".'.format(INFO_2, argument)))
        # label_4 - Python version number. Retrieved by calling function.
        self.label_4 = ttk.Label(self.frame_4, text=get_python_version())

        # Add label_2 to_4 into frame_4
        self.label_2.grid(row=0, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)
        self.label_3.grid(row=1, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)
        self.label_4.grid(row=2, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)

        # label_5 - Message for Close button
        self.label_5 = ttk.Label(self.frame_3, text="Close Application",
                                 style='small.TLabel')
        # Add label_5 to frame 3
        self.label_5.grid(row=0, column=0, padx=5, pady=5)

        # Create Buttons:
        # Button_1 Increment
        self.button_1 = ttk.Button(self.frame_2, text=BUTTON_1_TEXT,
                                   command=self.button_1_callback)
        # Button_2 Decrement
        self.button_2 = ttk.Button(self.frame_2, text=BUTTON_2_TEXT,
                                   command=self.button_2_callback)
        # Add button_1 and _2 to frame_2
        self.button_1.grid(row=0, column=0, padx=5, pady=5)
        self.button_2.grid(row=0, column=1, padx=5, pady=5)

        # Button_3 to Close
        self.button_3 = ttk.Button(self.frame_3, text=BUTTON_3_TEXT,
                                   command=self.button_3_callback)
        # Add button_3 to frame_3
        self.button_3.grid(row=1, column=0, padx=5, pady=5)

        # ===== Add frames to main 3 x 3 grid ===== #***
        self.frame_1.grid(row=0, column=0, columnspan=3)  # , sticky="WE")
        self.frame_2.grid(row=1, column=0, columnspan=2)  # , sticky="NS")
        self.frame_3.grid(row=1, column=2, columnspan=1)  # , sticky=E)
        self.frame_4.grid(row=2, column=0, columnspan=3)

        # ===== Initial Setup =====
        # Call function to perform initial setup of label_1
        main_program_action(self.label_1, "")

        # ===== End of all widget creation and setup =====

    # ===== Widget call backs =====
    def button_1_callback(self):
        """Increment Button - Call function main_program"""
        main_program_action(self.label_1, "inc")

    def button_2_callback(self):
        """Decrement Button - Call function main_program"""
        main_program_action(self.label_1, "dec")

    def button_3_callback(self):
        """Close the GUI application"""
        sys.exit()


def main_program_action(label_1, status):
    """
    This is the main section of program code. It has been placed outside of
    the GUI_Application() class.
    "label_1" is the self.label_1 in the GUI_Applications class. It is passed
    to this function so that the labels message and colours can be changed.
    "status" is either "inc" or "dec" from the button callback functions.
    """
    # Changed to increment and decrement a global variable integer
    global argument_1
    if status == "inc":
        argument_1 += 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:
            label_1.config(text=string, style='blue.TLabel')
        else:
            label_1.config(text=string, style='red.TLabel')

    elif status == "dec":
        argument_1 -= 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:
            label_1.config(text=string, style='blue.TLabel')
        else:
            label_1.config(text=string, style='red.TLabel')

    else:  # Don't increment or decrement. Use when launched.
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:
            label_1.config(text=string, style='blue.TLabel')
        else:
            label_1.config(text=string, style='red.TLabel')


def get_python_version():
    """
    Function to retrieve the python version.
    The python version number is the string of characters before the first
    space in the string returned from the function sys.version().
    E.g. "3.4.0"
    >>> sys.version
    '3.4.0 (default, Apr 11 2014, 13:05:11) \n[GCC 4.8.2]'
    """
    python_version = sys.version.split(" ")[0]
    return "Python version: {}.".format(python_version)

if __name__ == "__main__":
    """Check for command line argument. Launch GUI"""
    if len(sys.argv) > 1:
        argument_1 = sys.argv[1]
    else:
        argument_1 = 0
    # Provide help
    if argument_1 == "-h" or argument_1 == "--help":
        print("{} V{}. {}\n{}\n"
              "Use option --copy2bin create launchable program."
              .format(PROGRAM, VERSION, sys.argv[0], INFO_1))
        sys.exit()
    # Provide copy to /usr/local/bin/
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
    # Pass a value to launch program. Or 0 if no value.
    try:
        argument_1 = int(argument_1)
    except ValueError:
        # If not an integer then force to a value of 0
        argument_1 = 0

    print(TITLE_2)
    # Launch tkinter GUI.
    root = Tk()
    # Force the geometry of the GUI width x height + position x + position y
    # root.geometry('400x180+50+100')
    main_gui = GUI_Application(root, argument_1)
    root.mainloop()  # Tells Tk to enter its event loop.

"""
Notes:

=====
References:
https://python-textbok.readthedocs.org/en/1.0/Introduction_to_GUI_Programming.html
http://stackoverflow.com/questions/17125842/python-3-tkinter-change-label-text
https://www.tcl.tk/man/tcl8.5/TkCmd/contents.htm
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-element-layer.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-layouts.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html

=====
Setup the program so it can be launched from the command line:
Linux Instructions:
Note: Requires first line to be the shebang. E.g. #!/usr/bin/env python3

To convert a program so it can be run from the linux bash command line...
Copy to /usr/local/bin/ stripping the ".py" extension. Renaming if desired.
$ sudo cp python_file_name.py /usr/local/bin/program_name
E.g. $ sudo cp python_octal_calculator_v3.py /usr/local/bin/octalcalc

Set file to be executable.
$ sudo chmod +x /usr/local/bin/program_name
E.g. $ sudo chmod +x /usr/local/bin/octalcalc

Launch the program.
$ program_name
E.g. $ octalcalc

Example:
$ sudo cp program_01.py /usr/local/bin/program1
$ sudo chmod +x /usr/local/bin/program1
$ ls -l /usr/local/bin/program1
-rwxr-xr-x 1 root root 8702 Jan 27 10:50 /usr/local/bin/program1
$ program1

=====
#Obtaining TLabel options...
style = ttk.Style()
print("TLabel layout:\n{}".format(style.layout('TLabel')))
print("TLabel.border:\n{}".format(style.element_options('TLabel.border')))
print("TLabel.padding:\n{}".format(style.element_options('TLabel.padding')))
print("TLabel.label:\n{}".format(style.element_options('TLabel.label')))
sys.exit()

        # Obtain information of TWidgets layout and element_options, etc
        # print("TButton layout:\n{}".format(self.style.layout('TButton')))
        # print("TFrame layout:\n{}".format(self.style.layout('TFrame')))
        # [('Frame.border', {'sticky': 'nswe'})]
        # Frame.border
        # print("TFrame.border:\n{}"
        #      .format(self.style.element_options('TFrame.border')))
        # ('-background', '-borderwidth', '-relief')

TLabel layout:
[('Label.border', {'sticky': 'nswe', 'children':
    [('Label.padding', {'sticky': 'nswe', 'children':
        [('Label.label', {'sticky': 'nswe'})],
    'border': '1'})],
'border': '1'})]

TLabel.border:
('-background', '-borderwidth', '-relief')
TLabel.padding:
('-padding', '-relief', '-shiftrelief')
TLabel.label:
('-compound', '-space', '-text', '-font', '-foreground', '-underline',
'-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image',
'-stipple', '-background')

=====
#Obtaining TButton options...
style = ttk.Style()
print("TButton layout:\n{}".format(style.layout('TButton')))
print("TButton.border:\n{}".format(style.element_options('TButton.border')))
print("TButton.focus:\n{}".format(style.element_options('TButton.focus')))
print("TButton.padding:\n{}".format(style.element_options('TButton.padding')))
print("TButton.label:\n{}".format(style.element_options('TButton.label')))
sys.exit()

TButton layout:
[('Button.border', {'children':
    [('Button.focus', {'children':
        [('Button.padding', {'children':
            [('Button.label', {'sticky': 'nswe'})],
        'sticky': 'nswe'})],
    'sticky': 'nswe'})],
'sticky': 'nswe', 'border': '1'})]

TButton.border:
('-background', '-borderwidth', '-relief')
TButton.focus:
('-focuscolor', '-focusthickness')
TButton.padding:
('-padding', '-relief', '-shiftrelief')
TButton.label:
('-compound', '-space', '-text', '-font', '-foreground', '-underline',
'-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image',
'-stipple', '-background')

=====
Examples of performing a lookup on a style option.
print("TLabel border background colour: {}"
      .format(style.lookup('TLabel.border', 'background')))

TLabel border background colour: #d9d9d9

print("TLabel border borderwidth: {}"
      .format(style.lookup('TLabel.border', 'borderwidth')))

TLabel border borderwidth: 1

         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789

"""
