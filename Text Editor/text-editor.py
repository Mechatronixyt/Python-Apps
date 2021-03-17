from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
import random
opened_file = False
def new_file():
    text.delete(0.0,END)  #Deletes all the contents of the text editor.
    opened_file = False
def open_file():
    file1=filedialog.askopenfile(mode='r', initialdir = "/Files/", title = "Open File", filetypes = (
		("Text Files", "*.txt"), 
		("HTML", "*.html"), 
		("CSS", "*.css"), 
		("JavaScript", "*.js"), 
		("Java", "*.java"), 
		("Python", "*.py"), 
		("All Files", "*.*")
		)) #To open open_file filedialog.
    data=file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data) #Inserts data variable in text editor.
    opened_file = True
    opened_file_name = file1
def save_file():
    if opened_file:
    	filename= opened_file_name
    	data=text.get(0.0,END)
    	file1=open(filename,"w")
    	file1.write(data)
    else:
    	filename= str(random.randint(10000, 99999)) + ".txt"
    	data=text.get(0.0,END)
    	file1=open(filename,"w")
    	file1.write(data)
def save_as():
    try:
    	file1=filedialog.asksaveasfile(mode='w', defaultextension = ".*", initialdir = "/Files/", title = "Save Files As", filetypes = (
		("Text Files", "*.txt"), 
		("HTML", "*.html"), 
		("CSS", "*.css"), 
		("JavaScript", "*.js"), 
		("Java", "*.java"), 
		("Python", "*.py"), 
		("All Files", "*.*")
		)) #To open save_as filedialog.
    	data=text.get(0.0,END)
    	file1.write(data)
    except AttributeError:
    	messagebox.showwarning("Text Editor", "Oh we found an error ( ˘︹˘ )") 


gui=Tk() #For tkinter object.
gui.title("Text editor") 
gui.geometry("600x390")
#600 is length and 500 is breadth of the text editor.
gui.resizable(0, 0)
text=Text(gui)
text.pack() #To display the text in the centre.
mymenu=Menu()
list1=Menu(tearoff = False)
list1.add_command(label='New file',command=new_file) #To create menus.
list1.add_command(label='Open file',command=open_file)
list1.add_command(label='Save',command=save_file)
list1.add_command(label='Save as',command=save_as)
list1.add_command(label='Exit',command=gui.quit)
mymenu.add_cascade(label='File',menu=list1) #To create a file option.
gui.config(menu=mymenu)
gui.mainloop() #To display the window in the screen.This line is compulsory.
