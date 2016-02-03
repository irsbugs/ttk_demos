#!/usr/bin/env python3
#
# Program:      program_03b.py
#
# Objective:    GUI application template using buttons and labels
#               Uses program_3a.py
#               Introduces ttk RadioButton as arrays / lists
#               Change the style for the top set of radio buttons
#               Command line option 1 sets the default values of Radiobuttons
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Feb-02
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
PROGRAM = "program_03b.py"
VERSION = "1.0"
TITLE_1 = "GUI Application. {} {}".format(PROGRAM, VERSION)
TITLE_2 = "Launching tkinter/ttk application. {} {}".format(PROGRAM, VERSION)
INFO_1 = ("Program to highlight use of radiobutton arrays.\n"
          "Option of 1 will launch with pre-selected radio buttons.")
INFO_2 = "The command line argument was "
BUTTON_1_TEXT = "Submit"
BUTTON_3_TEXT = "Close"

# Define Variables:
argument_1 = 0  # For command line first argument (sys.argv[1]).
# *** Radio button array data
radiobutton_set_1_text = ["Oranges", "Lemons", "Grapes"]
radiobutton_set_1_value = ["orange", "lemon", "grape"]

radiobutton_set_2_text = ["One", "Two", "Three"]
radiobutton_set_2_value = [1, 2, 3]

radiobutton_set_3_text = ["Pi", "e"]
radiobutton_set_3_value = [3.141592, 2.718281]

# TODO: Combine the text and value data lists. E.g.
# radiobutton_set_3_data = [["Pi", 3.141592], ["e", 2.718281]]

# Main GUI application


class GUI_Application():

    def __init__(self, master, argument):
        """Setup the style, widgets and initial appearance on launching"""
        self.master = master
        master.title(TITLE_1)
        # Set String variable for Radiobutton set 1
        self.radiobutton_set_1 = StringVar()
        # Set Int variable for Radiobutton set 2
        self.radiobutton_set_2 = IntVar()
        # Set Float variable for Radiobutton set 3
        self.radiobutton_set_3 = DoubleVar()

        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()

        # Change a root style to modify all widgets.
        self.style.configure('.', font=('FreeSans', 12))

        # Create a Blue style for the label. Use when value 0
        self.style.configure('blue.TLabel', foreground='white',
                             background='#0000ff', font=('FreeSans', 16),
                             padding=10)

        # Create a Frame style
        self.style.configure('cyan.TFrame', borderwidth=5, relief="ridge",
                             background='#00ffff')

        # Create a RadioButton Style #***
        # print("TRadioButton layout:\n{}"
        #      .format(self.style.layout('TRadiobutton')))
        #
        # print("TRadiobutton.indicator:\n{}"
        #      .format(self.style.element_options('Radiobutton.label')))
        # TRadiobutton.indicator:
        # ('-background', '-indicatorcolor', '-indicatorrelief',
        # '-indicatordiameter', '-indicatormargin', '-borderwidth')
        # .focus = ('-focuscolor', '-focusthickness')
        # .padding = ('-padding', '-relief', '-shiftrelief')

        self.style.configure('red.TRadiobutton',
                             foreground='#ff0000', background='#cccccc',
                             indicatorcolor='#880000', indicatordiameter=20,
                             indicatormargin=5, indicatorrelief='raised',
                             borderwidth=3,
                             focuscolor='#0000ff', focusthickness=5
                             )
        self.style.map('red.TRadiobutton',
                       foreground=[('disabled', '#aaaaaa'),  # Light grey
                                   ('pressed', '#008800'),  # Mid Green
                                   ('active', '#00ff00')],  # Light Green
                       background=[('disabled', '#cccccc'),  # Light Grey
                                   ('pressed', '#00ff00'),  # Light Green
                                   ('active', '#008800')],  # Mid Green
                       highlightcolor=[('focus', 'green'),  # no effect?
                                       ('!focus', 'red')],  # no effect?
                       relief=[('pressed', 'sunken'),       # Also groove,
                               ('!pressed', 'raised')])     # flat and ridge

        # ===== Create Widgets =====

        # Create Frames
        # Frame1. Relief = "sunken" "flat" "groove" "ridge" "raised"
        self.frame_1 = ttk.Frame(master, style='cyan.TFrame',
                                 padding="5 5 5 5")
        # Create Labels:
        # label_1 - Main label to display the values of selected radiobuttons
        self.label_1 = ttk.Label(self.frame_1, text="", style='blue.TLabel')
        # Add label_1 into frame_1
        self.label_1.grid(row=0, column=0, sticky="WE")

        # Create Radiobutton array sets: #***
        self.radiobutton_array_1 = []
        for i in range(len(radiobutton_set_1_text)):
            self.radiobutton_array_1.append(ttk.Radiobutton(
                                            master,
                                            text=radiobutton_set_1_text[i],
                                            value=radiobutton_set_1_value[i],
                                            variable=self.radiobutton_set_1,
                                            command=self.radiobutton_1_cb,
                                            style='red.TRadiobutton'))

        self.radiobutton_array_2 = []
        for i in range(len(radiobutton_set_2_text)):
            self.radiobutton_array_2.append(ttk.Radiobutton(
                                            master,
                                            text=radiobutton_set_2_text[i],
                                            value=radiobutton_set_2_value[i],
                                            variable=self.radiobutton_set_2,
                                            command=self.radiobutton_2_cb))

        self.radiobutton_array_3 = []
        for i in range(len(radiobutton_set_3_text)):
            self.radiobutton_array_3.append(ttk.Radiobutton(
                                            master,
                                            text=radiobutton_set_3_text[i],
                                            value=radiobutton_set_3_value[i],
                                            variable=self.radiobutton_set_3,
                                            command=self.radiobutton_3_cb))

        # Create Button_1 - Submit the data
        self.button_1 = ttk.Button(master, text=BUTTON_1_TEXT,
                                   command=self.button_1_cb)
        # Create Button_3 - Close
        self.button_3 = ttk.Button(master, text=BUTTON_3_TEXT,
                                   command=self.button_3_cb)

        # ===== Add widgets to main grid =====
        # Add items from radiobutton arrays
        # ***program_03b iterates through the array
        for i in range(len(self.radiobutton_array_1)):
            self.radiobutton_array_1[i].grid(row=1, column=i, padx=10, pady=5,
                                             sticky=W)
        for i in range(len(self.radiobutton_array_2)):
            self.radiobutton_array_2[i].grid(row=2, column=i, padx=10, pady=5,
                                             sticky=W)
        for i in range(len(self.radiobutton_array_3)):
            self.radiobutton_array_3[i].grid(row=3, column=i, padx=10, pady=5,
                                             sticky=W)
        # Add frame with label and buttons
        self.frame_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.button_1.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.button_3.grid(row=4, column=2, padx=5, pady=5, sticky=E)

        # ===== Initial Setup =====
        # Perform initial setup of radiobuttons and invoke submit.
        # Command line option "1" will setup the default values
        if argument:
            self.radiobutton_set_1.set("lemon")
            self.radiobutton_set_2.set(3)
            self.radiobutton_set_3.set(3.141592)
            self.button_1.invoke()

        # ===== End of all widget creation and setup =====

    # ===== Widget call backs =====
    def radiobutton_1_cb(self):
        """Radio button set 1 callback. Place value from variable into Label"""
        # ***print(self.radiobutton_1_set.get())
        self.label_1.config(text=self.radiobutton_set_1.get())

    def radiobutton_2_cb(self):
        """Radio button set 2 callback. Place value from variable into Label"""
        self.label_1.config(text=self.radiobutton_set_2.get())

    def radiobutton_3_cb(self):
        """Radio button set 3 callback. Place value from variable into Label"""
        self.label_1.config(text=self.radiobutton_set_3.get())

    def button_1_cb(self):
        """Submit all data top the label"""
        self.label_1.config(text="{}, {}, {}"
                            .format(self.radiobutton_set_1.get(),
                                    self.radiobutton_set_2.get(),
                                    self.radiobutton_set_3.get()))

    def button_3_cb(self):
        """Close the GUI application"""
        sys.exit()


def main_program_action(label_1):
    """
    This is the main section of program code. It has been placed outside of
    the GUI_Application() class.
    "label_1" is the self.label_1 in the GUI_Applications class. It is passed
    to this function so that the labels text can be changed.
    """
    # This wont work as the radiobutton_set_n's are defined in the class
    # Would need to pass this data to this function. A bit pointless.
    self.label_1.config(text="{}, {}".format(self.radiobutton_set_1.get(),
                                             self.radiobutton_set_2.get()))


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
        argument_1 = False
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
print("TButton.border:\n{}".format(style.element_options('TButton.border')))Radiobutton.indicator
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

=====
TRadioButton layout:
[('Radiobutton.padding', {'sticky': 'nswe', 'children':
[('Radiobutton.indicator', {'sticky': '', 'side': 'left'}),
('Radiobutton.focus', {'sticky': '', 'children':
[('Radiobutton.label', {'sticky': 'nswe'})], 'side': 'left'})]})]

=====

         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789

"""
