import json
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import show

# Creating the window of  the gui
root = tk.Tk()
frm = ttk.Frame(root,padding = 80)
root.geometry("400x600")
frm.grid()



# The original File
test_json3 = "test2.json"



# Converting the json datas into python objects
def load_tasks():
    if not os.path.exists(test_json3):
        return []
    
    with open(test_json3,"r") as f:
        return json.load(f)


#  Converting all the python objects in Json data
def save_tasks(tasks):
    with open(test_json3 , "w") as f:
        json.dump(tasks,f,indent=4)


load_task = load_tasks()


# All placeholder value to put ghost text on entry
placeholder_add = "Add subject here"
placeholder_delete = "delete task here"
placeholder_update = "Update values here"
placeholder_key_add = "Add Key* here"
placeholder_key_remove = "Remove Key* here"
placeholder_key_search = "Search data here"


# All the entries for the options(add,delete,update,search)

# For add option(the entry bar)
add_entry = ttk.Entry(frm,width = 30)
add_entry.grid(column = 0 ,row = 0)

# For delete option(the entry bar)
delete_entry = ttk.Entry(frm,width = 30)
delete_entry.grid(column = 0 ,row = 2)

# For update option(the entry bar)
update_entry = ttk.Entry(frm,width = 30)
update_entry.grid(column = 0,row = 3)

# For add key option(the entry bar)
add_key_entry = ttk.Entry(frm,width = 30)
add_key_entry.grid(column = 0,row = 4)


# For remove key option(the entry bar)
remove_key_entry = ttk.Entry(frm,width = 30)
remove_key_entry.grid(column = 0,row = 5)

# For search key option(the entry bar)
search_key_entry = ttk.Entry(frm,width = 30)
search_key_entry.grid(column = 0, row = 6)



# This function is used to apply the ghost text on entry
def add_placeholder(entry,placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(foreground="gray")

# This function is used to remove the ghost text whenever the entry is clicked
def remove_placeholder(entry , placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(foreground="black")



# initial states when the entry bar of options is not clicked
add_entry.insert(0, placeholder_add)
add_entry.config(foreground="gray")

delete_entry.insert(0, placeholder_delete)
delete_entry.config(foreground="gray")

update_entry.insert(0, placeholder_update)
update_entry.config(foreground="gray")

add_key_entry.insert(0, placeholder_key_add)
add_key_entry.config(foreground="gray")

remove_key_entry.insert(0, placeholder_key_remove)
remove_key_entry.config(foreground="gray")

search_key_entry.insert(0, placeholder_key_search)
search_key_entry.config(foreground="gray")



# events to trigger the ghost text or remove it whenever the entry bar is clicked
add_entry.bind("<FocusIn>", lambda e: remove_placeholder(add_entry, placeholder_add))
add_entry.bind("<FocusOut>", lambda e: add_placeholder(add_entry, placeholder_add))

delete_entry.bind("<FocusIn>", lambda e: remove_placeholder(delete_entry, placeholder_delete))
delete_entry.bind("<FocusOut>", lambda e: add_placeholder(delete_entry, placeholder_delete))

update_entry.bind("<FocusIn>", lambda e: remove_placeholder(update_entry, placeholder_update))
update_entry.bind("<FocusOut>", lambda e: add_placeholder(update_entry, placeholder_update))

add_key_entry.bind("<FocusIn>", lambda e: remove_placeholder(add_key_entry, placeholder_key_add))
add_key_entry.bind("<FocusOut>", lambda e: add_placeholder(add_key_entry, placeholder_key_add))

remove_key_entry.bind("<FocusIn>", lambda e: remove_placeholder(remove_key_entry, placeholder_key_remove))
remove_key_entry.bind("<FocusOut>", lambda e: add_placeholder(remove_key_entry, placeholder_key_remove))

search_key_entry.bind("<FocusIn>" , lambda e : remove_placeholder(search_key_entry, placeholder_key_search))
search_key_entry.bind("<FocusOut>" , lambda e: add_placeholder(search_key_entry, placeholder_key_search))


# delete and destroy functions are used to give command to delete options(Buttons)


def delete(delete):
    global load_task
    load_task = [i for i in load_task if i["subject"] != delete]
    save_tasks(load_task)

def destroy():
    text = delete_entry.get()
    delete(text)


# update and updates functions are used to give command to update data of an index


def update():
    text = update_entry.get()
    text_list = text.split(" ")
    index = int(text_list[0])
    key = text_list[1]
    load_task[index][key] = text_list[2]
    save_tasks(load_task)

def updated():
    update()



# add_key and added_keys are commands for add key button/options to add a new parametre or key 


def add_key(key):
    for i in load_task:
        if key not in load_task:
            i[key] = "" 
    save_tasks(load_task)

def added_keys():
    text = add_key_entry.get()
    if text != "":
        add_key(text)

# remove_keys and remove_key are functions to remove an existing parameter or function


def remove_keys(key):
    for i in load_task:
        del i[key]
    save_tasks(load_task)

key_list = [i for i in load_task[0]]

def remove_key():
    text = remove_key_entry.get()
    remove_keys(text)


# Add key adds a new data or subject including its existing parameter(though it remains empty)


def add(add): 
    tasks = {"subject" : add,
        "done" : False}
    for new_keys in key_list:
        if new_keys not in tasks:
            tasks.update({new_keys : ""})
  
    load_task.append(tasks)
    save_tasks(load_task)


def submit():
    text = add_entry.get()
    if text != "":
        add(text)

# Search and search_data functions are used to search a subject with all its parameters(metadata)


    
def search(search):
    for i in load_task:
        if i["subject"] == search:
            for idx,key in enumerate(i):
                text = f"{key} : {i[key]}"
                search_label = ttk.Label(frm,text = text)
                search_label.grid(row = 8 +idx ,column = 0)
                print(text)

def search_data():
    text = search_key_entry.get()
    searches = text
    search(searches)

# This function is a command to clear the label appeared after searching


def destroy_labels():
    for widget in frm.winfo_children():
        if isinstance(widget,ttk.Label):
            widget.destroy()



# Buttons for each options(add,delete,update,add_key,remove_key,search)


add_button = ttk.Button(frm,text = "Add",command = submit )
add_button.bind("")
add_button.grid(column = 1 ,row = 0)

delete_button = ttk.Button(frm,text = "delete",command = destroy )
delete_button.grid(column = 1 ,row = 2)

update_button = ttk.Button(frm,text = "update",command = updated )
update_button.grid(column = 1 ,row = 3)

add_a_key_button = ttk.Button(frm,text = "Add key",command = added_keys )
add_a_key_button.grid(column = 1 ,row = 4)

remove_button = ttk.Button(frm,text = "Remove key",command = remove_key )
remove_button.grid(column = 1 ,row = 5)

search_button = ttk.Button(frm,text = "Search key" , command = search_data)
search_button.grid(column = 1 ,row = 6)

# Show button in the main.py gui will open another window in which you can view your data it is stored in show.py module

show_button = ttk.Button(frm,text = "Show Button",command = show.show_data )
show_button.grid(column = 1 ,row = 7)

Clear_button = ttk.Button(frm,text = "Clear",command = destroy_labels)
Clear_button.grid(column = 2 ,row = 6 )


#keeps the Graphical User Interface (GUI) visible, responsive, and continuously running


root.mainloop()
