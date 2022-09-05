import tkinter as tk
import customtkinter as ctk
import createClass
import leftFrameClass
import displayClass

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = ctk.CTk()
root.geometry("850x400")

leftFrame = leftFrameClass.leftFrameWindow(root)
displayFunc = displayClass.displayWindow(root,"wikipedia")


root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=20)
root.mainloop()
