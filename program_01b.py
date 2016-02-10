#!/usr/bin/env python3
#
# Program:      program_01b.py
#
# Objective:    GUI application template.
#               Standard GUI provides labels and a button
#               Feature GUI - On / Off buttons and styled label
#               Commence migration of functionality. Change:
#               main_program_outside_GUI, argument to be integer,
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Feb-10
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation
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
    import tkinter as tk
except ImportError as e:
    print("Import Error: {}".format(e))
    print("tkinter module for python3 is not available.")
    print("To install tkinter: $ sudo apt-get install python3-tk")
    sys.exit()
try:
    from tkinter import ttk
except ImportError as e:
    print("Import Error: {}".format(e))
    print("Import Error: tkinter.ttk module is not available.")
    print("To install tkinter: $ sudo apt-get install python3-tk")
    sys.exit()

# from tkinter import constants as C

# Define Constants - Standard Section:
PROGRAM = "program_01b.py"
VERSION = "2.0"
TITLE_1 = "GUI Application. {} {}".format(PROGRAM, VERSION)
TITLE_2 = "Launching tkinter/ttk application. {} {}".format(PROGRAM, VERSION)
INFO_1 = "Program to display which button is pressed."
INFO_2A = "No command line argument was passed on launching."
INFO_2B = "The command line argument was "
CLOSE_TEXT = "Close"

# Define Variables - Standard and Feature Section:
argument_1 = 0  # For command line first argument (sys.argv[1]). # ***

# Define Constants - Feature Section:
BUTTON_1_TEXT = "On"
BUTTON_2_TEXT = "Off"
ON_TEXT = "On"
OFF_TEXT = "Off"
# Define Variables - Feature Section:


# Main GUI application
class GUI_Application_Feature(ttk.Frame):

    def __init__(self, parent, argument):
        ttk.Frame.__init__(self, parent)
        """
        Initilization of GUI to feature more widgets
        """
        # self.parent = parent # <== not needed?
        self.create_feature_widgets(argument)
        self.action_on_launch(argument)

    # ===== Start for Feature Section =====
    def create_feature_widgets(self, argument):

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()

        # Create a Green style for the label when the On button is used
        self.style.configure('green.TLabel', foreground='black',
                             background='#00ff00', font=('FreeSans', 16),
                             padding=10)

        # Create a Red style for the label when the Off button is used
        self.style.configure('red.TLabel', foreground='white',
                             background='#ff0000', font=('FreeSans', 16),
                             padding=10)  # borderwidth=10)
        # Create more styles here...

        # ===== Create Widgets =====
        # Create Labels:
        # label_1 - Main label to display the status of the switches
        self.label_1 = ttk.Label(self, text="")

        # Create Buttons:
        # Button On
        self.button_1 = ttk.Button(self, text=BUTTON_1_TEXT,
                                   command=self.button_1_callback)
        # Button Off
        self.button_2 = ttk.Button(self, text=BUTTON_2_TEXT,
                                   command=self.button_2_callback)
        # Create more widgets here...

        # ===== Add widgets to grid =====
        self.label_1.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        self.button_1.grid(row=1, column=0, padx=10, pady=10)
        self.button_2.grid(row=1, column=2, padx=10, pady=10)

    def action_on_launch(self, argument):
        """Actions on initial launching of the application"""
        # Call function to perform initial setup of label_1
        # Pass the command line argument. E.g. "on" or "off" or ""
        main_program_outside_GUI_class(self.label_1, argument)
        # self.main_program_inside_GUI_class(argument)

    # ===== Widget call backs =====
    def button_1_callback(self):
        """On Button - Call function for on off buttons"""
        # Change commenting to choose between inside or outside of class
        main_program_outside_GUI_class(self.label_1, "on")
        # self.main_program_inside_GUI_class("on")

    def button_2_callback(self):
        """Off Button - Call function for on off buttons"""
        # Change commenting to choose between inside or outside of class
        main_program_outside_GUI_class(self.label_1, "off")
        # self.main_program_inside_GUI_class("off")

    def main_program_inside_GUI_class(self, status):
        """Calling to code in the loop saves having to pass widget info"""
        if status == "on":
            self.label_1.config(text=ON_TEXT, style='green.TLabel')
        elif status == "off":
            self.label_1.config(text=OFF_TEXT, style='red.TLabel')
        else:
            self.label_1.config(text="", style='TLabel')
    # ===== End of GUI Applications Class Feature section =====


def main_program_outside_GUI_class(label1, status):
    """
    This is the main section of program code. It has been placed outside of
    the GUI_Application() class.
    "label1" is the self.label_1 in the GUI_Applications class. It is passed
    to this function so that the labels text message and colour styles may be
    changed.
    "status" is either "on" or "off" from the button callback functions.
    """
    # if status == "on":
    #     label1.config(text=ON_TEXT, style='green.TLabel')
    # elif status == "off":
    #     label1.config(text=OFF_TEXT, style='red.TLabel')
    # else:
    #     label1.config(text="", style='TLabel')
    # ***
    global argument_1
    if status == "on":
        argument_1 += 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        label1.config(text=string, style='green.TLabel')

    elif status == "off":
        argument_1 -= 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))

        label1.config(text=string, style='red.TLabel')
    else:
        label1.config(text="", style='TLabel')


class GUI_Application_Standard(ttk.Frame):
    """Main GUI for the standard functionality"""

    def __init__(self, parent, argument):
        ttk.Frame.__init__(self, parent)
        """
        Initilization of GUI
        self is objects in this class
        parent is the root = tk.Tk
        """
        # self.parent = parent # <== not needed?
        self.master.title(TITLE_1)
        # print(dir(self)) # <== __init__ in tkinter?
        # print(dir(parent)) # <== root = tk.TK
        # print(dir(argument))
        self.create_standard_widgets(argument)
        # self.create_feature_widgets(argument)
        # self.action_on_launch(argument)

    def create_standard_widgets(self, argument):
        """Setup the style, widgets and initial appearance on launching"""

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()
        # Change a root style to modify all widgets.
        self.style.configure('.', font=('FreeSans', 12))

        # ===== Create Widgets =====
        # Create Labels:
        # label_1 - Program description
        self.label_1_standard = ttk.Label(self, text=INFO_1)
        # label_2 - State the argument if one was passed.
        if argument is None:
            self.label_2_standard = ttk.Label(self, text=(INFO_2A))
        else:
            self.label_2_standard = ttk.Label(self, text=('{} "{}".'
                                              .format(INFO_2B, argument)))
        # label_3 - Python version number. Retrieved by calling function.
        self.label_3_standard = ttk.Label(self, text=get_python_version())
        # label_4 - Spare - Not used
        self.label_4_standard = ttk.Label(self, text="")

        # Create Buttons:
        # Button to Close
        self.button_1_standard = ttk.Button(self, text=CLOSE_TEXT,
                                            command=self.button_1_standard_cb)

        # ===== Add widgets to grid =====
        # Labels
        self.label_1_standard.grid(row=0, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        self.label_2_standard.grid(row=1, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        self.label_3_standard.grid(row=2, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        self.label_4_standard.grid(row=3, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        # Buttons
        self.button_1_standard.grid(row=4, column=3, padx=10, pady=10,
                                    sticky="e")
        # ===== End of all standard widget creation and setup =====

    def button_1_standard_cb(self):
        """Callback from close button to close the GUI application"""
        sys.exit()


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
    """Check for command line argument. Provide copying to bin. Launch GUI"""
    print(TITLE_2)
    if len(sys.argv) > 1:
        argument_1 = sys.argv[1]
    else:
        argument_1 = 0  # Changed from None to 0 # ***

    # Provide help
    if argument_1 == "-h" or argument_1 == "--help":
        print("{} V{}. {}\n{}\n"
              "Use option --copy2bin create launchable program."
              .format(PROGRAM, VERSION, sys.argv[0], INFO_1))
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

    # If there is an argument_1, and its not -h --help or --copy2bin then the
    # argument will be passed to the GUI application.
    # Pass a value to launch program. Or 0 if no value. # ***
    try:
        argument_1 = int(argument_1)
    except ValueError:
        # If not an integer then force to a value of 0
        argument_1 = 0
    # Launch tkinter GUI.
    root = tk.Tk()

    # Force the geometry of the GUI width x height + position x + position y
    # root.geometry('1000x180+100+100')
    # Open the two GUI Application class. Use grid to place in different rows
    main_gui = GUI_Application_Standard(root, argument_1).grid(row=1, column=0)
    main_gui = GUI_Application_Feature(root, argument_1).grid(row=0, column=0)
    root.mainloop()

'''
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

print("TButton focus: {}"
      .format(style.lookup('TButton.focus', 'focuscolor')))

=====
Examples of performing a lookup on a style option.
print("TLabel border background colour: {}"
      .format(style.lookup('TLabel.border', 'background')))

TLabel border background colour: #d9d9d9

print("TLabel border borderwidth: {}"
      .format(style.lookup('TLabel.border', 'borderwidth')))

TLabel border borderwidth: 1

=====
    # ===== Main Program if it is included in the class GUI_Application() =====
    def button_on_off_action(self, status):
        """Change the message and colours"""
        if status == "on":
            self.label_1.config(text=ON_TEXT, style='green.TLabel')
        elif status == "off":
            self.label_1.config(text=OFF_TEXT, style='red.TLabel')
        else:
            self.label_1.config(text="", style='TLabel')

=====
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html
===
Widget class	Style name
Button 	        TButton
Checkbutton     TCheckbutton
Combobox 	    TCombobox
Entry 	        TEntry
Frame 	        TFrame
Label 	        TLabel
LabelFrame 	    TLabelFrame
Menubutton 	    TMenubutton
Notebook 	    TNotebook
PanedWindow     TPanedwindow (not TPanedWindow!)
Progressbar     Horizontal.TProgressbar or Vertical.TProgressbar,
                    depending on the orient option.
Radiobutton     TRadiobutton
Scale 	        Horizontal.TScale or Vertical.TScale,
                    depending on the orient option.
Scrollbar 	    Horizontal.TScrollbar or Vertical.TScrollbar,
                    depending on the orient option.
Separator 	    TSeparator
Sizegrip 	    TSizegrip
Treeview 	    Treeview (not TTreview!)

Ttk comes with 17 widgets, eleven of which already existed in tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow,
Radiobutton, Scale and Scrollbar.
The other six are new:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview.

* = tkinter widgets - not part of ttk widgets. Others to be investigated.
BaseWidget,
BitmapImage,
*Canvas,
Image,
*Listbox (Use ttk Combobox)
*Message,
*OptionMenu?,
PhotoImage,
*Spinbox,
Studbutton,
*Text,
Tributton,
Widget,
Wm,
Xview



LabelFrame and Labelframe seem to be the same. With ttk opt for First letter
uppercase and remaining letter lowercase.

>>> f = ttk.LabelFrame()
>>> fClass = f.winfo_class()
>>> fClass
'TLabelframe'

>>> f = ttk.Labelframe()
>>> fClass = f.winfo_class()
>>> fClass
'TLabelframe'

Same with PanedWindow and Panedwindow...

>>> p = ttk.PanedWindow()
>>> pClass = p.winfo_class()
>>> pClass
'TPanedwindow'
>>> p = ttk.Panedwindow()
>>> pClass = p.winfo_class()
>>> pClass
'TPanedwindow'
>>>



===
print(sys.path)

/home/ian/python_templates
/usr/lib/python3.4
/usr/lib/python3.4/plat-x86_64-linux-gnu
/usr/lib/python3.4/lib-dynload
/usr/local/lib/python3.4/dist-packages
/usr/lib/python3/dist-packages


===

         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789

'''
