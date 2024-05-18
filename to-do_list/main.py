import tkinter as tkinter
import tkinter.messagebox
from to_do_list import add_task, delete_task, save_task

# Initialize the main window
window = tkinter.Tk()
window.title("To-Do List")

# Create a frame
list_frame = tkinter.Frame(window)
list_frame.pack()

# Create listbox widget
task_box = tkinter.Listbox(window, width=40)
task_box.pack(side=tkinter.LEFT)

# Create scrollbar for the listbox
scroller = tkinter.Scrollbar(window)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# Configure the listbox and scrollbar to work together
task_box.config(yscrollcommand=scroller.set)
scroller.config(command=task_box.yview)

# Create the Entry widget for task input
task_entry = tkinter.Entry(window, width=50, text="ADDED TASKS")
task_entry.pack()

# Create the Add Task button
add_task_button = tkinter.Button(window, text="ADD", font=("arial", 20, "bold"), background="white", width=40, command=lambda: add_task(task_entry, task_box))
add_task_button.pack()

save_task_button = tkinter.Button(window, text="SAVE", font=("arial", 20, "bold"), background="white", width=40, command=lambda: save_task(task_box))
save_task_button.pack()

delete_task_button = tkinter.Button(window, text="Delete", font=("arial", 20, "bold"), background="white", width=40, command=lambda: delete_task(task_box))
delete_task_button.pack()

# Function to save tasks and close the window
def on_closing():
    save_task(task_box)
    window.destroy()

# Save tasks when the window is closed
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI main loop
window.mainloop()
