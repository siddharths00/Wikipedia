
from cgitb import text
from pyexpat import features
import tkinter as tk
from xml.sax.handler import feature_external_ges
import numpy as np

from fileinput import filename
import os
from myMarkdown import markdown
from tkhtmlview import HTMLLabel
from frame import Frame
from bs4 import BeautifulSoup

filename = "./articles/1.md"

directory = "./articles"

def raiseit(e,item):
    createTextFrame.delete(1.0,tk.END)
    displayTextFrame.set_html("")
    item.tkraise()


def modified(e,text,mylabel):
    text.edit_modified(0)
    print(e)
    mdText = text.get("1.0", tk.END)
    html = markdown(mdText)
    mylabel.set_html(html)
    text.edit_modified(0)


def display():
    fileobj = open(filename,'r')
    textMarkdown = fileobj.read();
    htmlText = markdown(textMarkdown)
    print("=========================================================")
    print("=========================================================")
    print(htmlText)
    print("=========================================================")
    print("=========================================================")
    displayFrame.set_html(htmlText)
    displayFrame.tkraise()


def saveit(e,text):
    filepath = directory +'/name.md'
    fileobj = open(filepath,'w')
    txt = text.get(1.0,tk.END)
    fileobj.write(txt)
    fileobj = open(filepath,'r')
    textMarkdown = fileobj.read();
    # print(textMarkdown)
    htmlText = markdown(textMarkdown)

    displayFrame.set_html(htmlText)

    displayMainFrame.getMaster().tkraise()

def editPressed(e):
    
    fileobj = open(filename,'r')
    text = fileobj.read();
    createTextFrame.insert(1.0,text)
    htmlText = markdown(text)

    displayTextFrame.set_html(htmlText)
    createMainWindow.getMaster().tkraise()

    

root = tk.Tk()

root.geometry("800x600")

############################################################################

# LEFT FRAME

############################################################################

leftFrame = Frame(root, 0, 0, "green", rowconfigure=[(0,1), (1,20)], columnconfigure=[(0,1)])

createFrame = Frame(leftFrame.getMaster(), 0, 0, "pink")

createButton = tk.Button(createFrame.getMaster(),text="Create Page")
createButton.grid(row=0,column=0)
#############################################################################

# RIGHT FRAME

#############################################################################

rightFrame = Frame(root, 0, 1, "green", rowconfigure=[(0,1)], columnconfigure=[(0,1)])

createMainWindow = Frame(rightFrame.getMaster(), 0, 0, rowconfigure=[(0,1)], columnconfigure=[(0,1),(1,1)])

createTextFrame = tk.Text(createMainWindow.getMaster())
createTextFrame.grid(row=0,column=0,sticky="NEWS")
displayTextFrame = HTMLLabel(createMainWindow.getMaster(),html="")
displayTextFrame.grid(row=0,column=1,sticky="NEWS")


createTextFrame.bind("<<Modified>>",lambda e: modified(e,createTextFrame,displayTextFrame))
createTextFrame.edit_modified(0)


saveButton = tk.Button(createMainWindow.getMaster(),text="save")
saveButton.grid(row=1,column=0)


cancelButton = tk.Button(createMainWindow.getMaster(),text="cancel")
cancelButton.grid(row=1,column=1)

displayMainFrame = Frame(rightFrame.getMaster(), 0, 0, rowconfigure=[(1,1)], columnconfigure=[(0,1)])


displayFrame = HTMLLabel(displayMainFrame.getMaster(),html="",background="brown")
displayFrame.grid(row=1,column=0,sticky="NEWS")

createButton.bind("<Button-1>",lambda e: raiseit(e,createMainWindow.getMaster()))
saveButton.bind("<Button-1>",lambda e: saveit(e,createTextFrame))
saveButton.grid(row=1,column=0)



editButton = tk.Button(displayMainFrame.getMaster(),text="Edit")
editButton.bind("<Button-1>",lambda e: editPressed(e))
editButton.grid(row=0,column=0)
display()
















root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=10)
root.mainloop()
