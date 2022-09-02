from msilib.schema import File
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from myMarkdown import markdown
from tkhtmlview import HTMLLabel
import createClass
import os

class displayWindow:
    filename = "wikipedia"
    directory = './articles/'
    text = ""
    def __init__(self,root,filename):
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


        self.title = ctk.CTkLabel(self.rightFrame,text= self.filename)
        self.title.grid(row=1,column=0)
        
        self.previewText = HTMLLabel(self.rightFrame,wrap=tk.WORD)
        self.previewText.grid(row=2,column=0,sticky="NEWS",columnspan=2)
        self.getData()
        self.previewTextscrollbar = ctk.CTkScrollbar(self.rightFrame, command=self.previewText.yview)
        self.previewTextscrollbar.grid(row=2, column=1, sticky="ens")
        self.previewText.configure(yscrollcommand=self.previewTextscrollbar.set)
        self.rightFrame.rowconfigure(2,weight=1)
        self.rightFrame.columnconfigure(0,weight=1)


    def removePage(self):
        if messagebox.askquestion('Ask Question',self.filename+' will be deleted') == 'yes':
            if self.filename == 'wikipedia':
                messagebox.showerror("error","You can't delete home page")
            else:
                os.remove(self.directory+self.filename+'.txt');
                messagebox.showinfo("info",self.filename+' deleted successfully')
                self.redirectToHome = displayWindow(self.root,"wikipedia")



    def getData(self):
        
        self.filepath = self.directory + self.filename +'.txt'
        self.file = open(self.filepath,'r')
        self.textToHtml = self.file.read()
        self.text = markdown(self.textToHtml)
        self.previewText.set_html(self.text)
        self.file.close()

    def editPressed(self):
        self.obj = createClass.createWindow(self.root,self.filename)

    def textAreaModified(self,e):
        self.textArea.edit_modified(0)
        self.text = self.textArea.get("1.0",tk.END)
        self.html = markdown(self.text)
        self.previewText.set_html(self.html)
        self.textArea.edit_modified(0)

    def saveTheFile(self):
        if messagebox.askquestion('Ask Question', 'Do you want to Save?') == 'yes':
            
            self.title = self.pageTitle.get()
            if self.title == '':
                messagebox.showerror('error',"Title can't be blank")
            else:
                self.directory = './articles/'
                self.filepath = self.directory + self.title+'.txt'
                self.fileText = self.textArea.get(1.0,tk.END)
                #print(self.fileText)
                self.file = open(self.filepath,'w')
                self.file.write(self.fileText)
                messagebox.showinfo("info","File saved successfully")
                



