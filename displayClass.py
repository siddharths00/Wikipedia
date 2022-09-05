"""

Display Class
=============
Display Class display the content of the specified file on screen.

"""


from msilib.schema import File
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from myMarkdown import markdown
from __init__ import *
import createClass
import leftFrameClass
import os

class displayWindow:
    filename = "wikipedia"
    """
    Default file to be displayed
    """
    directory = './articles/'
    """
    Globally declared directory
    """
    text = ""
    def __init__(self,root,filename=None):
        self.filename = filename
        self.root = root
        self.rightFrame = ctk.CTkFrame(self.root)
        self.rightFrame.grid(row=0,column=1,sticky="NEWS",padx=5,pady=5)

        self.buttonFrame = ctk.CTkFrame(self.rightFrame)
        self.buttonFrame.grid(row=0,column=0,sticky="NEWS",padx=10,pady=10)

        self.edit = ctk.CTkButton(self.buttonFrame,text="Edit",command = self.editPressed)
        self.edit.grid(row=0,column=0,pady=10,sticky="E",padx=10)
        self.remove = ctk.CTkButton(self.buttonFrame,text="Remove",command = self.removePage)
        self.remove.grid(row=0,column=1,pady=10,sticky="E",padx=10)

        self.setTitle(filename)
          
        self.previewText = HTMLLabel(self.rightFrame,wrap=tk.WORD,fobj=self)
        self.previewText.grid(row=2,column=0,sticky="NEWS",columnspan=2)
        self.getData()
        self.previewTextscrollbar = ctk.CTkScrollbar(self.rightFrame, command=self.previewText.yview)
        self.previewTextscrollbar.grid(row=2, column=1, sticky="ens")
        self.previewText.configure(yscrollcommand=self.previewTextscrollbar.set)
        self.rightFrame.rowconfigure(2,weight=1)
        self.rightFrame.columnconfigure(0,weight=1)


    def removePage(self):
        """
        This function removes or deletes the specified file.

        """
        if messagebox.askquestion('Ask Question',self.filename+' will be deleted') == 'yes':
            if self.filename == 'wikipedia':
                messagebox.showerror("error","You can't delete home page")
            else:
                os.remove(self.directory+self.filename+'.md');
                messagebox.showinfo("info",self.filename+' deleted successfully')
                self.newobj = leftFrameClass.leftFrameWindow(self.root)
                self.redirectToHome = displayWindow(self.root,"wikipedia")

    def setTitle(self,fname=None):
        """
        This function sets the title of the file by taking the filename as input.
        :Input:
              :fname: name of the file and title is set for it
        """
        if(fname): 
            self.filename=fname
            self.title = ctk.CTkLabel(self.rightFrame,text= self.filename)
            self.title.grid(row=1,column=0)
        

    def getData(self):
        """
            Fetches the data from the file to be displayed.
        """
        self.filepath = self.directory + self.filename +'.md'
        try:
            self.file = open(self.filepath,'r')
            self.textToHtml = self.file.read()
            self.text = markdown(self.textToHtml)
            self.previewText.set_html(self.text)
            self.file.close()
        except:
            if messagebox.askquestion('Ask Question', 'No such file exists, Do you want to create the file?') == 'yes':
                self.lobj=leftFrameClass.leftFrameWindow.createNewFile(self)
            
            


    def editPressed(self):
        """ 
            This opens the edit window whenever the edit button is clicked.
        """
        self.obj = createClass.createWindow(self.root,self.filename)


                



