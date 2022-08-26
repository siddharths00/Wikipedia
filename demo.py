# Import required modules
from tkinter import *
from tkinter import ttk
import os
import markdown
from tkhtmlview import HTMLLabel

# assign directory
directory = './articles'
from functools import partial

# Main tkinter window
x = Tk()
x.geometry("1000x700")
x.title("Wikipedia")

label1 = Label(x, text="Wikipedia", foreground="black", font=('bold', 26))
label1.pack(pady=20)

# The left side frame where the buttons are
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
a.place(rely=0.1, relheight=0.9, relwidth=0.1)

# This create function will run whenever we click on button. This will open a new
# window and will render the markdown.

def create(name): 
    # Open a new window on top of the window x.
    mainWindow = Toplevel(x)
    mainWindow.geometry("500x500")
        
    # menubar adds the file menu item in the new window
    menubar = Menu(mainWindow)
        
    menu_f = Menu(menubar,title='my title',tearoff=0) # file

    menubar.add_cascade(label="File", menu=menu_f) # Top Line

    # These do not have any functionality right now, we may add later
    # Look at this link https://www.plus2net.com/python/tkinter-text-editor.php    
    menu_f.add_command(label="Save")
    menu_f.add_command(label="Save As..")
    menu_f.add_command(label="Close and Discard")
    mainWindow.config(menu=menubar)
    
    # The following code reads the details of the file
    mainWindow.title(name)   # update the GUI title 
    fob=open(name,'r') # open in read more 
    my_str1=fob.read() # read data from file

    # convert markdown to html
    html = markdown.markdown(my_str1)
    
    # Render the HTML on screen
    my_label = HTMLLabel(mainWindow, html=html)
 
    # Adjust The rendered output
    my_label.grid(pady=20, padx=20)
    

# This function basically loops over all files inside of folder articles and
# creates as many buttons as there are files.
# This function created all the buttons on the main page of the GUI.
def func():
    index=1
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            # Each button will be named differently and clicking on each button
            # would call the create function and pass different file names as 
            # argument
            Button(a, text=filename+"\t  ", font=('bold', 8), command=partial(create, f)).grid(row=index, column=0, sticky=W)
            index+=1
        else:
            print("something wrong")


# The right side frame where there is nothing now
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.1, rely=0.1, relheight=0.9, relwidth=0.9)


func()
mainloop()