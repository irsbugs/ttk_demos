#!/usr/bin/env python3
#
# Program:      program_07a.py
#
# Objective:    GUI application template using buttons and labels
#               Use same overall layout as program_01.py
#               Introduce ttk.Combobox with LabelFrames
#               Command line option 1 sets the default values
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Feb-19
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation
# 2. *** indicates changes in this program over previous revision.
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
PROGRAM = "program_07a.py"
VERSION = "2.0"
TITLE_1 = "GUI Application. {} {}".format(PROGRAM, VERSION)
TITLE_2 = "Launching tkinter/ttk application. {} {}".format(PROGRAM, VERSION)
INFO_1 = ("Combobox widget read-only.\n"
          "Option of 1 will launch with pre-selected data.")
INFO_2 = "The command line argument was "
BUTTON_1_TEXT = "Submit"
CLOSE_TEXT = "Close"
# Define Variables:
argument_1 = 0  # For command line first argument (sys.argv[1]).
# Main GUI application


class GUI_Application_Feature(ttk.Frame):

    """Main GUI for the featured functionality"""

    def __init__(self, parent, argument):
        ttk.Frame.__init__(self, parent)
        # Method of packing main ttk.Frame
        self.pack(expand=Y, fill=BOTH)
        # self.grid(row=0, column=0)
        # Pack options:  after, anchor, before, expand, fill, in_, ipadx,
        #                 ipady, padx, pady, side.
        # Grid options:  column, columnspan, in_, ipadx, ipady, padx, pady,
        #                 row, rowspan, sticky
        self.master.title(TITLE_1)
        self.create_feature_widgets(argument)

    def create_feature_widgets(self, argument):
        """Setup variables, style, widgets for appearance on launching"""
        # *** Set Int variable for Checkbutton set 1
        self.combobox_1_text = StringVar()
        # *** Set Int variable for Checkbutton set 2
        self.entry_2_text = StringVar()

        # Drop down list for combobox
        self.combobox_1_list = ["root", "admin", "guest", "bob", "fred",
                                "mary", "molly", "polly", "dolly", "wally"]
        self.combobox_1_list = sorted(self.combobox_1_list)

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()

        # Change a root style to modify all widgets.
        self.style.configure('.', font=('FreeSans', 12))

        # Create a Blue style for the label. Use when value 0
        self.style.configure('blue.TLabel', foreground='white',
                             background='#0000ff', font=('FreeSans', 16),
                             padding=10)

        self.style.configure('cyan.TFrame', borderwidth=5, relief="ridge",
                             background='#00ffff')

        self.style.configure('grey.TEntry', foreground='grey', padding=5)

        self.style.configure('black.TEntry', foreground='black', padding=5)

        # ===== Create Widgets =====
        # Create Frames
        # Frame1. Relief = "sunken" "flat" "groove" "ridge" "raised"
        self.frame_1 = ttk.Frame(self, style='cyan.TFrame',
                                 padding="5 5 5 5")

        # Create Label Frame for entry_1
        self.labelframe_1 = ttk.Labelframe(self, text="Account (lower case)")

        # Create Combobox_1  # ***
        # Use register to define functions to validate and process invalid
        self.combobox_1 = ttk.Combobox(
            self.labelframe_1,
            textvariable=self.combobox_1_text,
            height=5,
            width=10,
            validate='key',
            state="readonly",  # readwrite
            values=self.combobox_1_list,
            validatecommand=(self.register(self.is_valid_combo_1), '%P'),
            invalidcommand=(self.register(self.is_invalid_combo_1), '%W', '%P')
            )

        # To have a default value from the list selected.
        # self.combobox_1.current(0)  # First item
        # self.combobox_1.current(len(self.combobox_1_list)-1)  # Last item

        self.combobox_1.grid(in_=self.labelframe_1, row=0, column=0, padx=5,
                             pady=5)

        # Create Label Frame for entry_2
        self.labelframe_2 = ttk.LabelFrame(self, text="Password")
        # Create Entry_2 as though it is a password:
        self.entry_2 = ttk.Entry(self.labelframe_2,
                                 textvariable=self.entry_2_text,
                                 show="*"
                                 )
        # Setup the entry_2 inside the label_frame_2
        # self.entry_1.pack(fill=X, expand=Y, padx='1m', pady='1m')
        self.entry_2.grid(in_=self.labelframe_2, row=0, column=0, padx=5,
                          pady=5,)

        # Create Labels:
        # label_1 - Main label to display the status of the switches
        self.label_1 = ttk.Label(self.frame_1, text="", style='blue.TLabel')
        # Add label_1 into frame_1
        self.label_1.grid(row=0, column=0, sticky="WE")

        # Button_1 Submit the data
        self.button_1 = ttk.Button(self, text=BUTTON_1_TEXT,
                                   command=self.button_1_cb)

        # ===== Add frames to main grid =====
        # ***
        self.labelframe_1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.labelframe_2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # self.entry_2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        # self.checkbutton_2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.frame_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.button_1.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        # ===== Initial Setup =====
        # Setup default value of combobox based on argument.
        if argument >= 0 and argument < len(self.combobox_1_list):
            self.combobox_1.current(argument)
        # ===== End of all widget creation and setup =====

    # ===== Widget call backs =====
    def is_valid_combo_1(self, txt):
        """Check that text is alphabetical and lower case"""
        if txt.isalpha():
            if txt.islower():
                return True
            else:
                return False
        else:
            return False

    def is_invalid_combo_1(self, widget_name, txt):
        """Called whenever is_valid_entry_1() returns false"""
        # non-lowercase letters have been prevented from being added to entry_1
        # Make the bell warning sound
        # >>> [m for m in dir(str) if m.startswith('is')]
        # ['isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
        #  'isupper']
        widget = self.nametowidget(widget_name)
        widget.bell()
        widget.focus_set()

    def button_1_cb(self):
        """Submit all data top the label"""
        # print(self.entry_1_text.get())
        self.label_1.config(text="{},{}".format(
                            self.combobox_1_text.get(),
                            self.entry_2_text.get()
                            ))
        # Change from Grey to Black font in Entry_1
        # self.entry_1.configure(style='black.TEntry')


def main_program_action(label_1):
    """
    This is the main section of program code. It has been placed outside of
    the GUI_Application() class.
    "label_1" is the self.label_1 in the GUI_Applications class. It is passed
    to this function so that the labels text can be changed.
    """
    # Not worth passing the data out of the class.
    pass


class GUI_Application_Standard(ttk.Frame):

    """Main GUI for the standard functionality"""

    def __init__(self, parent, argument):
        ttk.Frame.__init__(self, parent)
        # Method of packing main ttk.Frame
        self.pack(expand=Y, fill=BOTH)
        # self.grid(row=1, column=0)

        self.master.title(TITLE_1)
        self.create_standard_widgets(argument)

    def create_standard_widgets(self, argument):
        """Setup the style, widgets and initial appearance on launching"""

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()
        # Change a root style to modify all widgets.
        self.style.configure('.', font=('FreeSans', 12))

        # ===== Create Widgets =====
        # Create Frame1 to place around labesl and close buttons  # ***
        self.frame_1 = ttk.Frame(self, padding="10 10 10 10", borderwidth=5,
                                 relief="ridge")
        # Frame within a frame for a close button  # ***
        self.frame_2 = ttk.Frame(self.frame_1,
                                 padding="10 10 10 10", borderwidth=5,
                                 relief="ridge")

        # Create Labels:
        # label_1 - Program description
        self.label_1_standard = ttk.Label(self.frame_1, text=INFO_1)
        # label_2 - State the argument if one was passed.
        self.label_2_standard = ttk.Label(self.frame_1,
                                          text=('{} "{}".'.format(INFO_2,
                                                                  argument)))
        # label_3 - Python version number. Retrieved by calling function.
        self.label_3_standard = ttk.Label(self.frame_1,
                                          text=get_python_version())

        # Create Buttons:
        # Button to Close
        self.button_1_standard = ttk.Button(self.frame_2, text=CLOSE_TEXT,
                                            command=self.button_1_standard_cb)

        # ===== Add widgets to grid =====
        # Labels
        self.label_1_standard.grid(row=0, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        self.label_2_standard.grid(row=1, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        self.label_3_standard.grid(row=2, column=0, columnspan=3, padx=5,
                                   pady=5, sticky="w")
        # Buttons
        # Add Close Button into its own frame, frame2
        self.button_1_standard.grid(row=0, column=0)

        # Frames
        # Add frame2 (with button) into frame1  # ***
        self.frame_2.grid(row=3, column=2, sticky="e")

        # Add master frame1 to the main ttk.frame at bottom  # ***
        self.frame_1.grid(row=1, column=0)
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
    # Open the two GUI Application class.
    main_gui = GUI_Application_Feature(root, argument_1)
    main_gui = GUI_Application_Standard(root, argument_1)
    root.mainloop()  # Tells Tk to enter its event loop.

"""
Notes:

=====
References:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Combobox.html
http://pyinmyeye.blogspot.co.nz/2012/08/tkinter-entry-with-validation-demo.html
http://www.tcl.tk/man/tcl8.4/TkCmd/entry.htm#M12
http://effbot.org/zone/tkinter-entry-validate.htm
http://stupidpythonideas.blogspot.co.nz/2013/12/tkinter-validation.html
http://stackoverflow.com/questions/18741078/ttk-entry-widget-validate-entry-invalid-text-entry-does-not-cause-reverting
http://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter
http://stackoverflow.com/questions/17635905/ttk-entry-background-colour
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Checkbutton.html
https://python-textbok.readthedocs.org/en/1.0/Introduction_to_GUI_Programming.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Checkbutton.html
https://python-textbok.readthedocs.org/en/1.0/Introduction_to_GUI_Programming.html
http://stackoverflow.com/questions/17125842/python-3-tkinter-change-label-text
https://www.tcl.tk/man/tcl8.5/TkCmd/contents.htm
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-element-layer.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-layouts.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html

=====

#     valid percent substitutions (see first link above)
#         %d = Type of action (1=insert, 0=delete, -1 for others)
#         %i = index of char string to be inserted/deleted, or -1
#         %P = value of the entry if the edit is allowed
#         %s = value of entry prior to editing
#         %S = the text string being inserted or deleted, if any
#         %v = the type of validation that is currently set
#         %V = the type of validation that triggered the callback
#              (key, focusin, focusout, forced)
#         %W = the tk name of the widget

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
