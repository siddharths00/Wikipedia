
from cgitb import text
from pyexpat import features
import tkinter as tk
from xml.sax.handler import feature_external_ges
import numpy as np

from fileinput import filename
import os
import markdown
from tkhtmlview import HTMLLabel

from bs4 import BeautifulSoup

filename = "./articles/1.md"

directory = "./articles"

class Frame:
    
    def __init__(self, master, row, column, background=None, rowconfigure=[], columnconfigure=[]):
        self.frame = tk.Frame(master, background=background)
        self.frame.grid(row=row, column=column, sticky="NEWS")
        
        for index, weight in rowconfigure:
            self.frame.rowconfigure(index=index,weight=weight)    
        
        for index, weight in columnconfigure:
            self.frame.columnconfigure(index=index,weight=weight)
        
        # (self.frame).canvas.configure(scrollregion=self.canvas.bbox("all"))

    
    def getMaster(self):
        return self.frame