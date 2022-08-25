# from tkinter import *
# from tkinter import messagebox
# # from db import Database

# # db = Database('store.db')

# # def select_item(event):
# #     try:
# #         global selected_item
# #         index = parts_list.curselection()[0]
# #         selected_item = parts_list.get(index)

# #         part_entry.delete(0, END)
# #         part_entry.insert(END, selected_item[1])
# #         customer_entry.delete(0, END)
# #         customer_entry.insert(END, selected_item[2])
# #         retailer_entry.delete(0, END)
# #         retailer_entry.insert(END, selected_item[3])
# #         price_entry.delete(0, END)
# #         price_entry.insert(END, selected_item[4])
# #     except IndexError:
# #         pass


# # def remove_item():
#     # db.remove(selected_item[0])
#     # clear_text()
#     # populate_list()


# # def update_item():
#     # db.update(selected_item[0], part_text.get(), customer_text.get(),
#     #           retailer_text.get(), price_text.get())
#     # populate_list()


# # def clear_text():
#     # part_entry.delete(0, END)
#     # customer_entry.delete(0, END)
#     # retailer_entry.delete(0, END)
#     # price_entry.delete(0, END)


# # Create window object
# app = Tk()

# # Part
# part_text = StringVar()
# part_label = Label(app, text='Part Name', font=('bold', 8), pady=20)
# part_label.grid(row=0, column=0, sticky=W)
# part_entry = Entry(app, textvariable=part_text)
# part_entry.grid(row=0, column=1)
# # Customer
# customer_text = StringVar()
# customer_label = Label(app, text='Customer', font=('bold', 8))
# customer_label.grid(row=1, column=0, sticky=W)
# customer_entry = Entry(app, textvariable=customer_text)
# customer_entry.grid(row=1, column=1)
# # Retailer
# retailer_text = StringVar()
# retailer_label = Label(app, text='Retailer', font=('bold', 8))
# retailer_label.grid(row=2, column=0, sticky=W)
# retailer_entry = Entry(app, textvariable=retailer_text)
# retailer_entry.grid(row=2, column=1)
# # Price
# price_text = StringVar()
# price_label = Label(app, text='Price', font=('bold', 8))
# price_label.grid(row=3, column=0, sticky=W)
# price_entry = Entry(app, textvariable=price_text)
# price_entry.grid(row=3, column=1)
# # Parts List (Listbox)
# parts_list = Listbox(app, height=8, width=50, border=0)
# parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# # Create scrollbar
# scrollbar = Scrollbar(app)
# scrollbar.grid(row=3, column=3)
# # Set scroll to listbox
# parts_list.configure(yscrollcommand=scrollbar.set)
# scrollbar.configure(command=parts_list.yview)
# # Bind select
# # parts_list.bind('<<ListboxSelect>>', select_item)

# # Buttons
# add_btn = Button(app, text='Add Part', width=12)
# add_btn.grid(row=4, column=0, pady=20)

# remove_btn = Button(app, text='Remove Part', width=12)
# remove_btn.grid(row=4, column=1)

# update_btn = Button(app, text='Update Part', width=12)
# update_btn.grid(row=4, column=2)

# clear_btn = Button(app, text='Clear Input', width=12)
# clear_btn.grid(row=4, column=3)

# app.title('Part Manager')
# app.geometry('700x350')

# # Populate data
# # populate_list()

# # Start program
# app.mainloop()


# # To create an executable, install pyinstaller and run
# # '''
# # pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# # '''

# Python program to
# Illustrate Separator
# widget


# Import required modules
from tkinter import *
from tkinter import ttk
import os
# assign directory
directory = './articles'
from functools import partial

# Main tkinter window
x = Tk()
x.geometry("400x300")
x.title("Wikipedia")

label1 = Label(x, text="Wikipedia", foreground="black", font=('bold', 26))
label1.pack(pady=20)

# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(rely=0.1, relheight=0.9, relwidth=0.1)


# Separator object
# separator = ttk.Separator(x, orient='vertical')
# separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)
# separator.grid(row=0, column=0, pady=20)

def func(pr):
    print(pr)
    index=1
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            print(f)
            Button(b, text='Part Name4', font=('bold', 8)).grid(row=index, column=0, sticky=W)
            index+=1
        else:
            print("something wrong")

# Label Widget
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
a.place(relx=0.1, rely=0.1, relheight=0.9, relwidth=0.9)
# a.place(relx=0.2, rely=0.1, relheight=0.8, relwidth=0.8)

# Button(b, text='Part Name', font=('bold', 8)).grid(row=0, column=0, sticky=W)
# Button(b, text='Part Name2', font=('bold', 8)).grid(row=2, column=0, sticky=W)
# Button(b, text='Part Name3', font=('bold', 8)).grid(row=4, column=0, sticky=W)

# Button(b, text='Part Name4', font=('bold', 8), command=partial(func, "arg")).grid(row=0, column=2, sticky=W)

# https://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter

part_entry = Entry(a, textvariable=StringVar())
part_entry.grid(row=0, column=1)

# configfile = Text(f3, wrap=WORD, width=45, height= 20)
# something = Text(a, height = 5, width = 52).grid(row=0, column=1, sticky=W)
with open("./articles/1.txt", 'r') as f:
    print(f.read())
    st = f.read()
    # something.insert(0,"st")
    part_entry.insert(0, "st")

func("outside")
mainloop()

# import required module


# iterate over files in
# that directory
     


# from tkinter import *
# import os

# def open():
#     os.system("start D:\\Wikipedia\\articles\\1.txt")

# root = Tk()
# button = Button(root, text="Open File Direction", command=open)
# button.pack()
# root.mainloop()