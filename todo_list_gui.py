import Tkinter as tk
from task_classes import Task, TaskList

#Creates frame
top = tk.Tk()
my_task_list = TaskList()
#DO NOT TOUCH ANYTHING ABOVE THIS
top.title("To-Do List")
#1. Iterate over not_done
for task in my_task_list.not_done:
    b = tk.Checkbutton(top, text = task.description, bg = "yellow")
    b.pack()

#1. Iterate over done
for task in my_task_list.done:
    var = tk.StringVar()
    label = tk.label = tk.Label( top, textvariable=var, relief=tk.RAISED, bg = "pink" )
    #Printing description
    var.set(task.description)
    label.pack()

#DO NOT TOUCH ANYTHING BELOW THIS
top.mainloop()