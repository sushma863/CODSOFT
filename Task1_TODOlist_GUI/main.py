import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


#  SAVE TASKS 
def save_tasks():
    tasks = []

    for index in range(listbox.size()):
        task_text = listbox.get(index)

        completed = task_text.startswith("✓ ")

        task = {
            "title": task_text[2:] if completed else task_text,
            "completed": completed
        }

        tasks.append(task)

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


# LOAD TASKS
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)

            for task in tasks:
                title = task["title"]

                if task["completed"]:
                    title = "✓ " + title

                listbox.insert(tk.END, title)

    except:
        pass


# ADD TASK
def add_task():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    listbox.insert(tk.END, task)

    entry.delete(0, tk.END)

    save_tasks()


# DELETE TASK
def delete_task():
    try:
        selected_task = listbox.curselection()[0]

        listbox.delete(selected_task)

        save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task to delete!")


# COMPLETE TASK
def complete_task():
    try:
        selected_task = listbox.curselection()[0]

        task_text = listbox.get(selected_task)

        if not task_text.startswith("✓ "):
            listbox.delete(selected_task)

            listbox.insert(selected_task, "✓ " + task_text)

            save_tasks()

    except:
        messagebox.showwarning("Warning", "Select a task!")


# GUI WINDOW 
root = tk.Tk()

root.title("To-Do List App")

root.geometry("500x500")

root.config(bg="#f0f0f0")


# TITLE
title = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="#333"
)

title.pack(pady=10)


# ENTRY 
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)

entry.pack(pady=10)


# BUTTON FRAME 
button_frame = tk.Frame(root, bg="#f0f0f0")

button_frame.pack(pady=10)


# ADD BUTTON
add_button = tk.Button(
    button_frame,
    text="Add Task",
    width=12,
    bg="#4CAF50",
    fg="white",
    command=add_task
)

add_button.grid(row=0, column=0, padx=5)


# COMPLETE BUTTON
complete_button = tk.Button(
    button_frame,
    text="Complete",
    width=12,
    bg="#2196F3",
    fg="white",
    command=complete_task
)

complete_button.grid(row=0, column=1, padx=5)


# DELETE BUTTON
delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=12,
    bg="#f44336",
    fg="white",
    command=delete_task
)

delete_button.grid(row=0, column=2, padx=5)


# TASK LIST
listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=15,
    selectbackground="#a6a6a6"
)

listbox.pack(pady=20)


# LOAD SAVED TASKS
load_tasks()


# RUN APP
root.mainloop()