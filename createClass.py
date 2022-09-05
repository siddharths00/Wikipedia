"""
Create Class
=============
This class contains the sekleton of the create window.
This also functions as edit window.


"""

from ctypes.wintypes import WORD
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from myMarkdown import markdown
from __init__ import *
import displayClass
import leftFrameClass
class createWindow:
    """
    Inputs:
        :root: the root object
        :type of root: this is the root widget
        :filename: name of the file when working as edit file and empty when called to create new file
        :type of filename: string

    """


    def __init__(self,root,filename):
        self.filename = filename
        self.root = root
        self.rightFrame = ctk.CTkFrame(self.root,fg_color="pink")
        self.rightFrame.grid(row=0,column=1,sticky="NEWS",padx=5,pady=5)
        self.createFrame = ctk.CTkFrame(root)
        self.createFrame.grid(row=0,column=1,sticky="NEWS",padx=5,pady=5)
        self.title = ctk.CTkLabel(self.createFrame,text="Title",text_font =('',20))
        self.title.grid(row=0,column=0,sticky="W")
        self.pageTitle = ctk.CTkEntry(self.createFrame,text_font=("",20))
        self.pageTitle.insert(0,self.filename)
        self.pageTitle.grid(row=1,column=0,sticky="EW",columnspan=2)
        
        
        self.textArea = tk.Text(self.createFrame,wrap=tk.WORD)
        self.textArea.grid(row=2,column=0,sticky="NEWS",columnspan=1,padx=5,pady=5)


        self.previewText = HTMLLabel(self.createFrame,wrap=tk.WORD)
        self.previewText.grid(row=2,column=1,sticky="NEWS",columnspan=1,padx=(10,30))
        self.textAreascrollbar = ctk.CTkScrollbar(self.createFrame, command=self.textArea.yview)
        self.textAreascrollbar.grid(row=2, column=0, sticky="ens")
        self.textArea.configure(yscrollcommand=self.textAreascrollbar.set)

        self.textArea.bind("<<Modified>>",lambda e: self.textAreaModified(e))
        self.textArea.edit_modified(0)
        self.previewTextscrollbar = ctk.CTkScrollbar(self.createFrame, command=self.previewText.yview)
        self.previewTextscrollbar.grid(row=2, column=1, sticky="ens",padx=(10,30))

        self.previewText.configure(yscrollcommand=self.previewTextscrollbar.set)

        if self.filename != '':
            self.getFileData(self.filename)
        self.savePage = ctk.CTkButton(self.createFrame,padx=5,pady=10,height=35,text="Save",command = self.saveTheFile)
        self.savePage.grid(row = 3,column = 1,sticky="E")
        

        self.createFrame.rowconfigure(1,weight=1)
        self.createFrame.rowconfigure(2,weight=50)
        self.createFrame.columnconfigure(0,weight=1)
        self.createFrame.columnconfigure(1,weight=1)

    def getFileData(self,filename):
        """
        This method write  the contents of the sepecfied file 
        
        Inputs : 
               :filename: name of the file to be opened
               :type of filename: string

        """
        self.directory = './articles/'
        self.filepath = self.directory + filename+'.md'        
        self.file = open(self.filepath,'r')
        self.text = self.file.read()
        self.textArea.insert(1.0,self.text)
        self.previewText.set_html(self.text)


    def textAreaModified(self,e):
        """
        Whenever the text gets updated this method updates the code on the preview screen.
        Inputs: 
              :event: Object of the event
              :type of event: Object of type event

        """
        self.textArea.edit_modified(0)
        self.text = self.textArea.get("1.0",tk.END)
        self.html = markdown(self.text)
        self.previewText.set_html(self.html)
        self.textArea.edit_modified(0)

    def saveTheFile(self):
        """This gets called when we save the file."""
        if messagebox.askquestion('Ask Question', 'Do you want to Save?') == 'yes':
            
            self.title = self.pageTitle.get()
            if self.title == '':
                messagebox.showerror('error',"Title can't be blank")
            else:
                self.directory = './articles/'
                self.filepath = self.directory + self.title+'.md'
                
                self.file = open(self.filepath,'w')
                
                self.fileText = self.textArea.get(1.0,tk.END)
                self.file.write(self.fileText)
                self.file.close()
                self.filename = self.title                
                self.newobj = leftFrameClass.leftFrameWindow(self.root)
                self.obj = displayClass.displayWindow(self.root,self.filename)
                messagebox.showinfo("info","File saved successfully")
                




