#Assign list
to_do_list = []
completed = []

from datetime import datetime

class Task(object):
    def __init__(self, description, completed, subject, date):
        self.completed = completed
        self.description = description
        self.subject = subject
        self.date = date
    now = datetime.now()
    def is_due(self):
        pass

    def task_summary(self):
        print self.description
        print self.subject
        print
    synopsis = Task("Read chapters 12-17 ")
    print synopsis.description
    print '%s/%s/%s' % ( now.month, now.day, now.year,)
    #is it due now?
#implement print method for task
#Description of to-do
#Date
#Is completed
#Subject it belongs to
    def print_tasks():
        print to_do_list
    mylist = Task("Walk Leo, Return book, Get groceries, Write card. ")
    print mylist
    print '%s/%s/%s' % (now.month, now.year,)

    def add_task():
        task = raw_input("What is your task? ")
        to_do_list.append(task)
    task = Task("Math HW ")
    print task
    print '%s/%s/%s' % (now.month, now.day, now.year,)

    def print_enumerated_tasks(self):
        for i, task in enumerate(to_do_list):
            print i, task

    def complete_task():
        print_enumerated_tasks()
        task_index = int(raw_input("To complete a task, type the number of that task. "))
        task = to_do_list.pop(task_index)
        completed.append(task)

    def view_completed():
        print completed

    def remove_task():
        print_enumerated_tasks()
        task_index = int(raw_input("To remove a task, type the number of that task. "))
        to_do_list.pop(task_index)



while (True):
    # casting the string input to an integer
    option = int(raw_input("Choose an option:\n"
                           "1. Add a task\n"
                           "2. Print tasks\n"
                           "3.Remove a task\n"
                           "4. Complete a task\n"
                           "5. View your completed tasks\n"
                           "6. Exit app\n"))
    # 1. Add a task

    if option == 1:
        add_task()
    # 2. Print Tasks
    elif option == 2:
        print_tasks()
    #Remove a task
    elif option == 3:
        remove_task()
    #4. Complete a task
    elif option == 4:
        complete_task()
    #5: View completed tasks
    elif option == 5:
        view_completed()
    # 6. Exit
    elif option == 6:
        break
    else:
        print "I don't know."
#HW:
    # Datetime lesson
    #Import datetime into project
    #Create instances of task
    #print method




