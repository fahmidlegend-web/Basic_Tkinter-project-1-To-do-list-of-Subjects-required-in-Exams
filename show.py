from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import os

done_btn  = None
btn_list = []


### The whole function works when you click show button in the gui of main.py
def show_data():
    root_show = tk.Toplevel()


    show_file = "test2.json"
    frm = ttk.Frame(root_show , padding = 80)
    style = ttk.Style()
    root_show.geometry("600x400")
    frm.grid()


    def load_tasks():
        if not os.path.exists(show_file):
            return []
            
        with open(show_file,"r") as f:
            return json.load(f)
    
    def save_tasks(tasks):
        with open(show_file , "w") as f:
            json.dump(tasks,f,indent=4)
           
    load_task = load_tasks()


    # The done function is used to set the paramter done true based on finished subject(by clicking done button) 

    def done(index):
        load_task[index]["done"] = True
        save_tasks(load_task)

    ### To show the datas(subject,percentage and grades) actually after clicking buttons
    
    def show_list(key):
        global done_btn
        global btn_list
        for widget in frm.winfo_children():
            if isinstance(widget,ttk.Label):
                widget.destroy()
        
        # if you click button other than subject, the done buttons get destroyed
        if done_btn is not None:
            for i in btn_list:
                i.destroy()
            btn_list.clear()
            done_btn = None
    
        # done buttons are created only when show subject is clicked, If you want to set it for a differeent parameter like(subject code,percentage etc) then you can change the statement
        if key == "subject":
            print("Hello subject")
            for idx,item in enumerate(load_task):
                done_btn = ttk.Button(frm, text=f"Done {item['subject']}",command = lambda idx = idx: done(idx))
                btn_list.append(done_btn)
                done_btn.grid(row= idx + 1 , column= 1)


        for i,items in enumerate(load_task):
            show_items = ttk.Label(frm,text = f"{i})  {items[key]}")
            show_items.grid(column =0  ,row = i + 1)
            
    # A list to store the key names
    list_keys = [i for i in load_task[0]]



    # add_button function is used to create the buttons called show subject,show done to click on datas related to the subject lists

    def add_button():
        for i,t in enumerate(list_keys):
            show_buttons = ttk.Button(frm,text = f"show {list_keys[i]}",command = lambda t = t : show_list(t))
            show_buttons.grid(column = i + 1 ,row = 0 )

    add_button()

    root_show.mainloop() 



