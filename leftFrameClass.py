import tkinter as tk
import customtkinter as ctk
import createClass
import os
import displayClass
from functools import partial
class leftFrameWindow:
    directory = "./articles"
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
        
        self.files=os.listdir(self.directory)
        self.index=0
        for file in self.files:
            self.justname = file.split(".")
            self.button= ctk.CTkButton(self.bottomFrame,text = file,bg_color="#262626",fg_color= "#262626",command=partial(displayClass.displayWindow, self.root, self.justname[0]))
            self.button.grid(row=self.index,column=0,pady=5,sticky="EW")
            self.index = self.index+1
        

    def displayTheFile(self,e,filename):
        self.transfername = filename
        self.fileobj = displayClass.displayWindow(self.root,self.transfername)
    def createNewFile(self):
        self.obj = createClass.createWindow(self.root,"")
