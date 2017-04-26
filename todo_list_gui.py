import Tkinter as tk
from task_classes import Task, TaskList

#Creates frame
top = tk.Tk()
my_task_list = TaskList()
#DO NOT TOUCH ANYTHING ABOVE THIS

#1. Iterate over not_done
for task in my_task_list.not_done:
    var = tk.StringVar()
    label = tk.Label(top, textvariable=var, relief=tk.RAISED)
    #Printing description
    var.set(task.description)
    label.pack()

#3. Make each element into a label


#DO NOT TOUCH ANYTHING BELOW THIS
top.mainloop()