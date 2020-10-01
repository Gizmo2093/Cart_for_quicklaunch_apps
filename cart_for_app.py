import tkinter
from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.title("Cart apps")
root.geometry("620x200")

#my_dir = os.getcwd()                      --- Get directory project
#root.iconbitmap(my_dir + r"\package.ico") --- Your icon here

# Create widget Listbox (this is Tuple)
my_listbox = Listbox(width=70,bd=2)
my_listbox.place(x=15, y=15)

# Open and read our saving list wiht app
if os.path.isfile('save.txt'):
    with open('save.txt','r') as file_object:
        for i in file_object:
            i_str = i.rstrip('\n')
            my_listbox.insert(END,i_str)


#add apps
def add_app():
    app = filedialog.askopenfilename(initialdir="/", title="Select app", filetypes=(("All files", "*.*"), ("exe", "*.exe")))
    if app == "":
        pass
    else:
        my_listbox.insert([0],app)
    

#launch avery app in our list
def start_app():
    for i in my_listbox.get(0,END):
        os.startfile(i)


# delete select item in list
def delete_app():
    selection = my_listbox.curselection()
    my_listbox.delete(selection[0])

# save our list
def save_app():
    with open('save.txt', 'w') as f:
        for i in my_listbox.get(0, END):
            f.write(i + "\n")


#buttons
btn_open = Button(root, text="Launch", fg='white', bg='#24AE36',width=18, command=start_app)
btn_open.place(x=450,y=15)

btn_add = Button(root, text="Select app", fg='white', bg='#2D3276',width=18, command=add_app)
btn_add.place(x=450,y=60)

btn_delete = Button(root,text='Delete',fg='white', bg='#CC372D',width=18, command=delete_app)
btn_delete.place(x=450, y=105)

btn_save = Button(root,text='Save list',fg='white', bg='#2D3276',width=18, command=save_app)
btn_save.place(x=450, y=150)


root.mainloop()