import tkinter as tkinter
import pickle


def add_task(task_entry, task_box):
    task = task_entry.get()
    if task != "":
        task_box.insert(tkinter.END, task)
        task_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(task_box):
    try:
        index_todo = task_box.curselection()[0]
        task_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning("Attention!!", "No task selected for deletion.")

def save_task(task_box):
    tasks = task_box.get(0, tkinter.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
