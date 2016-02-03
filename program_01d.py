#!/usr/bin/env python3
#
# Program:      program_01d.py
#
# Objective:    GUI application template using buttons and labels
#               Change the GUI aspects of program_01c.py.
#               Make the enable/disable button a toggle button using "state"
#
# Written for:  Hamilton Python User Group - Presentation xxx 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Jan-27
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation
# 2. #*** indicates a change between program_1a and program_1b
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
PROGRAM = "program_01d.py"  # ***
VERSION = "1.0"
TITLE_1 = "GUI Application. {} {}".format(PROGRAM, VERSION)
TITLE_2 = "Launching tkinter/ttk application. {} {}".format(PROGRAM, VERSION)
INFO_1 = "Program to display squares and cubes. Toggle button"
INFO_2B = "The command line argument value used: "
BUTTON_1_TEXT = "Increment"
BUTTON_2_TEXT = "Decrement"
BUTTON_3_TEXT = "Close"
BUTTON_4_TEXT = "Disable"

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

        # Create a Green style for the label is positive
        self.style.configure('green.TLabel', foreground='black',
                             background='#00ff00', font=('FreeSans', 16),
                             padding=10)
        # Create a Red style for the label is negative
        self.style.configure('red.TLabel', foreground='white',
                             background='#ff0000', font=('FreeSans', 16),
                             padding=10)  # borderwidth=10)
        # Create a Blue style for the label is 0  #***
        self.style.configure('blue.TLabel', foreground='white',
                             background='#0000ff', font=('FreeSans', 16),
                             padding=10)

        # Create a Green style Button for Increment
        self.style.configure('green.TButton', foreground='black',
                             background='#00ff00', font=('FreeSans', 16),
                             padding=10, focuscolor='#008800')
        # Create a Red style Button for Decrement
        self.style.configure('red.TButton', foreground='white',
                             background='#ff0000', font=('FreeSans', 16),
                             padding=10)  # borderwidth=10)

        # Create a inc style for Increment button
        self.style.configure('inc.TButton',
                             background='#004400',  # Dark Green background
                             foreground='#008800',  # Mid Green characters
                             borderwidth=5,  # bevelling amount raised button
                             highlightthickness='20',  # no effect?
                             font=('FreeSans', 18, 'bold'))
        self.style.map('inc.TButton',
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

        # Create a dec style for Decrement button
        self.style.configure('dec.TButton',
                             background='#440000',  # Dark Red background
                             foreground='#880000',  # Mid Red characters
                             borderwidth=5,  # bevelling to the raised button
                             highlightthickness='20',  # no effect?
                             font=('FreeSans', 18, 'bold'))
        self.style.map('dec.TButton',
                       foreground=[('disabled', '#aaaaaa'),  # Light grey
                                   ('pressed', '#880000'),
                                   ('active', '#ff0000')],  # Light Red
                       background=[('disabled', '#cccccc'),  # Light Grey
                                   ('pressed', '#ff0000'),
                                   ('active', '#880000')],  # Mid Red
                       highlightcolor=[('focus', 'green'),  # no effect?
                                       ('!focus', 'red')],  # no effect?
                       relief=[('pressed', 'sunken'),       # Also groove,
                               ('!pressed', 'raised')])     # ridge flat
        # ===== Create Widgets =====
        # Create Labels:
        # label_1 - Main label to display the status of the switches
        self.label_1 = ttk.Label(master, text="")
        # label_2 - Program description
        self.label_2 = ttk.Label(master, text=INFO_1)
        # label_3 - State the argument if one was passed.
        self.label_3 = ttk.Label(master, text=('{} "{}".'
                                               .format(INFO_2B, argument)))
        # label_4 - Python version number. Retrieved by calling function.
        self.label_4 = ttk.Label(master, text=get_python_version())

        # Create Buttons:
        # Button Increment
        self.button_1 = ttk.Button(master, text=BUTTON_1_TEXT,
                                   command=self.button_1_callback,
                                   style='inc.TButton')
        # Button Decrement
        self.button_2 = ttk.Button(master, text=BUTTON_2_TEXT,
                                   command=self.button_2_callback,
                                   style='dec.TButton')
        # Button to Close
        self.button_3 = ttk.Button(master, text=BUTTON_3_TEXT,
                                   command=self.button_3_callback)
        # Button to toggle Enable / Disable #***
        self.button_4 = ttk.Button(master, text=BUTTON_4_TEXT,
                                   command=self.button_4_callback)

        # ===== Add widgets to grid =====
        # Labels
        self.label_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.label_2.grid(row=2, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)
        self.label_3.grid(row=3, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)
        self.label_4.grid(row=4, column=0, columnspan=3, padx=5, pady=5,
                          sticky=W)

        # Buttons
        self.button_1.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.button_2.grid(row=1, column=1, padx=10, pady=10)
        self.button_3.grid(row=5, column=3, padx=10, pady=10)
        self.button_4.grid(row=5, column=0, padx=10, pady=10)
        # ===== Initial Setup =====
        # Call function to perform initial setup of label_1
        main_program_action(self.label_1, "")  # ***
        # ===== End of all widget creation and setup =====

    # ===== Widget call backs =====
    def button_1_callback(self):
        """On Button - Call main program function """
        main_program_action(self.label_1, "inc")  # ***

    def button_2_callback(self):
        """Off Button - Call main program function """
        main_program_action(self.label_1, "dec")  # ***

    def button_3_callback(self):
        """Close the GUI application"""
        sys.exit()

    def button_4_callback(self):
        disabled = self.button_1.state(['disabled'])
        # *** Returns tuple (!disabled,) when not disabled. i.e. Length = 1
        # When enabled returns tuple of (). i.e. Length = 0
        # print(len(disabled), disabled)

        if len(disabled) == 1:
            # Currently not disabled so disable.
            self.button_1.state(['disabled'])
            self.button_2.state(['disabled'])
            self.button_4.configure(text="Enable")  # Toggle the button text
        else:
            # Currently disabled so enable
            self.button_1.state(['!disabled'])
            self.button_2.state(['!disabled'])
            self.button_4.configure(text="Disable")  # Toggle the button text


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
    if status == "inc":  # ***
        argument_1 += 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:
            label_1.config(text=string, style='blue.TLabel')
        else:
            label_1.config(text=string, style='red.TLabel')

    elif status == "dec":  # ***
        argument_1 -= 1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:  # ***
            label_1.config(text=string, style='blue.TLabel')
        else:
            label_1.config(text=string, style='red.TLabel')

    else:  # Don't increment or decrement. Use when launched.
        string = ("{0} squared = {1}, {0} cubed = {2}"
                  .format(argument_1, argument_1**2, argument_1**3))
        if argument_1 > 0:
            label_1.config(text=string, style='green.TLabel')
        elif argument_1 == 0:  # ***
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
        argument_1 = 0   # *** Changed from None to 0
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
    root.mainloop()

'''
Notes:
Changes from program_01a.py to program_01b.py

#INFO_2A = "No command line argument was passed on launching." #***
INFO_2B = "The command line argument value used: " #***
BUTTON_1_TEXT = "Increment" #***
BUTTON_2_TEXT = "Decrement" #***
#ON_TEXT = "On" #***
#OFF_TEXT = "Off" #***

===
#*** Add for 0 value
self.style.configure('blue.TLabel', foreground='white',
                     background='#0000ff', font=('FreeSans', 16),
                     padding=10)
===
#if argument == None: #***
#    self.label_3 = ttk.Label(master, text=(INFO_2A)) #***
#else: #***
self.label_3 = ttk.Label(master, text=('{} "{}".'
                         .format(INFO_2B, argument)))

===
# Labels
self.label_1.grid(row=0, column=0, columnspan=3, padx=5, pady=5) #***
===
# Call function to perform initial setup of label_1
main_program_action(self.label_1, "")  #***

===
def button_1(self):
    """On Button - Call main program function """
    main_program_action(self.label_1, "inc") #***

def button_2(self):
    """Off Button - Call main program function """
    main_program_action(self.label_1, "dec") #***

===
if status == "inc": #***
elif status == "dec": #***
===
elif argument_1 == 0: #***
    label_1.config(text=string, style='blue.TLabel')
===

===== =====
Changes from program_01.py to program_01a.py
===
PROGRAM = "program_01a.py" #***
===
argument_1 = 0 #***  # For command line first argument (sys.argv[1]).
===
main_program_on_off_action(self.label_1, "on")  #*** Initial setup
===
    #*** New main program
    global argument_1
    if status == "on":
        argument_1 +=1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                .format(argument_1, argument_1**2, argument_1**3))
        label_1.config(text=string, style='green.TLabel')

    elif status == "off":
        argument_1 -=1
        string = ("{0} squared = {1}, {0} cubed = {2}"
                .format(argument_1, argument_1**2, argument_1**3))

        label_1.config(text=string, style='red.TLabel')
    else:
        label_1.config(text="", style='TLabel')

===
    #*** Modify Handling of command line input to check its an integer
    if len(sys.argv) > 1:
        argument_1 = sys.argv[1]
        try: #*** Test if integer was supplied from the command line
            argument_1 = int(argument_1)  #***
        except ValueError:  #***
            argument_1 = 0  #*** Was not an integer. Force to be integer of 0.
    else:
        argument_1 = 0  #*** Changed from None to 0

===

style = ttk.Style()
print("TButton focus colour: {}"
      .format(style.lookup('TButton', 'focuscolor')))
print("TButton focus thickness: {}"
      .format(style.lookup('TButton', 'focusthickness')))

print("TLabel border borderwidth: {}"
      .format(style.lookup('TLabel.border', 'borderwidth')))
print("TLabel border borderwidth: {}"
      .format(style.lookup('TLabel', 'borderwidth')))

print("TButton border background: {}"
      .format(style.lookup('TButton.border', 'background')))
print("TButton label background: {}"
      .format(style.lookup('TButton.label', 'background')))
print("TButton label bordercolor: {}"
      .format(style.lookup('TButton', 'bordercolor')))
print("Button.highlight:\n{}".format(style.element_options('TButton.label')))
print("Button.highlight:\n{}".format(style.map('TButton', 'label.background')))

#print("Button.highlight:\n{}".format(ttk.Button.cget('ttk.Button','background')))
#print(dir(ttk.Style.theme_names('*')))

#print("Button.highlight:\n{}".format(ttk.Style.theme_names()))

#sys.exit()

=====
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html

active 	    The mouse is currently within the widget.
alternate 	This state is reserved for application use.
background 	Under Windows or MacOS, the widget is located in a window that is
            not the foreground window.
disabled 	The widget will not respond to user actions.
focus 	    The widget currently has focus.
invalid 	The contents of the widget are not currently valid.
pressed 	The widget is currently being pressed (e.g., a button that is
            being clicked).
readonly 	The widget will not allow any user actions to change its current
            value. For example, a read-only Entry widget will not allow
            editing of its content.
selected 	The widget is selected. Examples are checkbuttons and radiobuttons
            that are in the “on” state.


=====
References:
https://python-textbok.readthedocs.org/en/1.0/Introduction_to_GUI_Programming.html
http://stackoverflow.com/questions/17125842/python-3-tkinter-change-label-text
https://www.tcl.tk/man/tcl8.5/TkCmd/contents.htm
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-element-layer.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-layouts.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html

         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789

'''
