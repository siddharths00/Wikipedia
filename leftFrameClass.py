"""
LeftFrameClass
===============
Left frame class handles the left part of the screen which contains
create and lists of all available files of wikipedia.

"""

import tkinter as tk
import customtkinter as ctk
import createClass
import os
import displayClass
from tkinter.messagebox import showinfo
from functools import partial
class leftFrameWindow:
    directory = "./articles"
    """
    This is globally declared directory which has all the files.
    """
    def __init__(self,root) :
        self.root = root
        self.leftFrame = ctk.CTkFrame(self.root)
        self.leftFrame.grid(row=0,column=0,sticky="NEWS",padx = 5,pady=5)
        self.leftFrame.columnconfigure(0,weight=1)
        self.leftFrame.rowconfigure(0,weight=1)
        self.leftFrame.rowconfigure(1,weight=20)
        self.topFrame = ctk.CTkFrame(self.leftFrame)
        self.topFrame.grid(row=0,column=0,sticky="NEWS",padx=5,pady=5)
        self.topFrame.columnconfigure(0,weight=1)
        self.createButton = ctk.CTkButton(self.topFrame,text="Create Page",command=self.createNewFile)
        self.createButton.grid(row=0,column=0,pady=20)

        self.bottomFrame = ctk.CTkFrame(self.leftFrame)
        self.bottomFrame.grid(row=1,column=0,sticky="NEWS",padx=5,pady=5)
        self.bottomFrame.columnconfigure(0,weight=1)
        self.bottomFrame.rowconfigure(0,weight=1)
        
        self.files=os.listdir(self.directory)
        listbox = tk.Listbox(self.bottomFrame,font=('Helveticabold 13'),fg="blue",bg="white", cursor="hand2")


        listbox.grid(row=0,column=0,columnspan=2,sticky="news")
        listboxscrollbar = ctk.CTkScrollbar(self.bottomFrame, command=listbox.yview)
        listboxscrollbar.grid(row=0,column=1, sticky="news")
        listbox.configure(yscrollcommand=listboxscrollbar.set)

        self.index=0
        for file in self.files:
            self.justname = file.split(".")
            listbox.insert(self.index,self.justname[0])
            self.index = self.index+1
        listbox.bind('<<ListboxSelect>>',lambda e:self.items_selected(e,listbox))
        
    def items_selected(self,e,listbox):
        """
        This function takes the input as the listbox widget which is list of all the files in the article folder.
        Displays the file when a particular link is clicked.
        :Input:
              :listbox: listbox which contains all the files in articles folder
        """
        selected_indices = listbox.curselection()
        if selected_indices==():
            return
        selected_file = ",".join([listbox.get(i) for i in selected_indices])
        displayClass.displayWindow(self.root,selected_file)

    def displayTheFile(self,e,filename):
        """
        This function display the file when a particular link is clicked.
        It takes as input the name of the file to be displayed.
        :Input:
              :filename: name of the file to be displayed
              :type of filename: string
        """
        self.transfername = filename
        self.fileobj = displayClass.displayWindow(self.root,self.transfername)

    def createNewFile(self):
        """
        This function gets called whenever we want to create a new file.
        """
        self.obj = createClass.createWindow(self.root,"")
