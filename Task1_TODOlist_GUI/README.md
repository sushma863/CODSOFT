# To-Do List GUI Application

A simple and user-friendly To-Do List application built using Python and Tkinter.
This application helps users manage daily tasks efficiently with features like adding tasks, marking tasks as completed, deleting tasks, and saving tasks permanently.

# Features
1 Add new tasks  
2 Mark tasks as completed  
3 Delete tasks  
4 Automatically save tasks  
5 Load saved tasks when application starts  
6 Simple and clean graphical user interface (GUI)
#  Technologies Used
-Python
- Tkinter (GUI)
- JSON
- File Handling
#  Project Structure
todo_app/
│
├── main.py
├── tasks.json
└── README.md

#  How to Run the Project
## Step 1: Install Python
Download Python from:
https://www.python.org/downloads/
During installation, make sure to check:
```text
Add Python to PATH
```
## Step 2: Open Project in VS Code
Open the project folder in Visual Studio Code.
## Step 3: Run the Application
Open terminal in VS Code and run:
bash
py main.py
or
python main.py
# Permanent Task Storage
All tasks are saved automatically inside:
```text
tasks.json
```
Example:

```json
[
  {
    "title": "Study Python",
    "completed": true
  },
  {
    "title": "Finish project",
    "completed": false
  }
]
```
# How to Use
##  Add Task
1. Enter task name
2. Click **Add Task**
## Complete Task
1. Select task from list
2. Click **Complete**
Completed tasks will show:
```text
✓ Study Python
```
## Delete Task
1. Select task
2. Click **Delete**
# Application Preview
Main Features:
- Add tasks
- Complete tasks
- Delete tasks
- Save automatically
# Concepts Used
- Python Functions
- Tkinter GUI
- Lists
- Dictionaries
- JSON Handling
- File Handling
- Event Handling
Developed using Python and Tkinter.