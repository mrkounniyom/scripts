#!/usr/bin/env python3

# Imports

import orgnode, datetime



# gui part

from tkinter import *

from tkinter import ttk

from tkinter import font

from tkinter import filedialog

from tkinter.messagebox import showinfo


# Start Gui Declarations ################################

root = Tk()

globalFont ="helvetica 13"

root.title("Org Mode")

frm = ttk.Frame(root, padding=10, width=200, height=50)

frm.grid()

mainFrame = ttk.Frame(frm, width=122, height=15)

textFrame = ttk.Frame(frm, width=122, height=15)

buttonFrame = ttk.Frame(frm, width=122, height=15)



# Text Area

text_area = Text(textFrame, height=15, width=122, padx = 5, relief=GROOVE, font=globalFont)

textFrame.grid(column=0, row=1)

text_area.pack(side=LEFT)


# End Gui Declarations ################################

#today = datetime.date.today()
#print "Daily plan for", today
#print "-------------------------\n"


# global variables #########################################
nodelist = ''
spacing = '   '
############################################################

def loadFile(filename):
    global nodelist, text_area
    #filename = '/home/mk/Documents/personal.org'
    #filename = "test.org"
    nodelist = orgnode.makelist(filename)
    text_area.insert(INSERT, '> Viewing ' + filename + ' <')
    text_area.insert(INSERT, '\n')

def save_file():
    global text_area
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    text2save = str(text_area.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.


def headingTab(node):
    """
    returns number of tabs for the heading.
    """
    global spacing
    headlvl = node.Level()-1
    head = ""

    for i in range(0,headlvl):
        head = head + spacing
    return head



def bodyTab(node):

    """
    returns number of tabs for the body.
    """
    global spacing
    headlvl = node.Level()
    head = ""

    for i in range(0,headlvl):
        head = head + spacing
    return head


# print Headings + body
def print_nodes():
    """
    prints nodes into text_area
    """
    global nodelist, text_area
    if text_area.get('1.0', 'end') != '':
        text_area.delete('1.0', 'end')
    for n in nodelist:

        #text_area.insert(INSERT, headingTab(n) + '*' + n.Heading() + '\n')
        text_area.insert(INSERT, headingTab(n) + n.Heading() + '\n')
        #text_area.insert(INSERT, bodyTab(n) + '*' + n.Body())
        text_area.insert(INSERT, bodyTab(n) + n.Body())
        text_area.insert(INSERT, '\n')



# Prints Lists items

# for n in nodelist:

    # head = headingTab(n)

    # head = head + n.Heading()

    # print(head)

    # for item in n.List():

        # print(item)

# open files
def open_file():
    """
    Opens filedialog
    """
    filetypes = (
        ('org files', '*.org'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir='.',
        filetypes=filetypes)

    loadFile(filename)
    print_nodes()

# Insert Buttons
q = ttk.Button(buttonFrame, text="Quit", command=root.destroy)
o = ttk.Button(buttonFrame, text="Open", command=open_file)
s = ttk.Button(buttonFrame, text="Save", command=save_file)

buttonFrame.grid(column=3, row=1)

q.pack(side=BOTTOM, pady=5, padx=2)
o.pack(side=BOTTOM, pady=5, padx=2)
s.pack(side=BOTTOM, pady=5, padx=2)

open_file()
root.mainloop()
