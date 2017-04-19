from datetime import date

#^^This imports date from the datetime library
class Task(object):
    """ Holds methods for setting a due date, assigning a subject and synopsis of your task"""
    def __init__(self, description, completed, subject, date):
        """__init__ initializes things so that they can be used in dot notation
                param: self, description (description for task, str), completed (if task has been completed, bool), subject (suject of task, str)and date(date for task, date)
        :return: none """
        self.completed = completed
        self.description = description
        self.subject = subject
        self.date = date
    def is_due(self):
        """This method makes it so that the user if they still have time for their task
        param: none
        :return: if your task is overdue or if you still have time, bool."""
        return date.today() >= self.date
    def get_task_summary(self):
        """
        Will format tasks for saving
        :return: string, comma separated values (description, completed, subject and date)
        """
        return self.description + "," + str(self.completed) + "," + self.subject + "," + str(self.date)

    def __str__(self):
        """ formats task for printing
        param: none
        :return: formatted task (str)"""
        return str(self.description)


class TaskList(object):
    """Holds lists of done and not done tasks"""
    def __init__(self):
        self.not_done = []
#        A list for tasks that are not done
        self.done = []
#       A list for tasks that are done
    def add_task(self, new_task):
        """Adds the task to the TaskList. If the task is completed, add it to done, otherwise, its added to not_done
        :param new_task: (Task) a Task object to add to the list
        :return: None
        """
        if new_task.completed:
            self.done.append(new_task)
        else:
            self.not_done.append(new_task)


    def remove_task(self, index):
        """removes tasks from a list
        param: index(int)
        :return: None"""
        if index < len(self.not_done) and index >= 0:
             self.not_done.pop(index)
        else:
            print "This is not a valid index- type the number of the task you want to remove."

    def complete_task(self, index):
        """completes a task
        param: index(int)
        :return: None"""
        if index < len(self.not_done) and index >= 0:
            completed_task = self.not_done.pop(index)
            completed_task.completed = True
            self.done.append(completed_task)
        else:
            print "This is not a valid index. "

    def sort_tasks(self, sort_by):
        """Sorts tasks by subject or date
        param: sort_by(str)
        :return: none'"""
        if sort_by == "subject":
            #TODO: homework March 7
            pass
        elif sort_by == "date":
            #TODO: homework March 7
            pass
        else:
            print "This isn't supported!"

    def print_tasks(self):
        for i, task in enumerate(self.not_done):
            print i, task

    def print_done_list(self):
        for t in self.done:
            print t

def add_task():
    """adds your task to your list
            param: none
        :return: prints out yout task"""
    task = raw_input("What is your task? ")
    to_do_list.append(task)


# instance of task list object
my_task_list = TaskList()

f = open("tasks.txt", "r")
for line in f:
    #This is splitting my saved strings into variables that are compatible with my task list.
    line_split = line.split(",")
    description = line_split[0]
    completed_str = line_split[1]
    completed_task = True
    if completed_str == "False":
        completed_task = False
    #This creates my instance of Task, and formats it correctly.
    new_class_task = Task(description, completed_task, "", date.today())
    #This adds my new instance of Task, new_class_task to my task list.
    my_task_list.add_task(new_class_task)
f.close()

while (True):
    # casting the string input to an integer
    option = int(raw_input("Choose an option:\n"
                           "1. Add a task\n"
                           "2. Print tasks\n"
                           "3.Remove a task\n"
                           "4. Complete a task\n"
                           "5. View your completed tasks\n"
                           "6. Exit app and save\n"
                           "7. Exit app. WILL NOT SAVE!!!\n"))
    # 1. Add a task
    if option == 1:
        task_description = raw_input("What is your task description?")
        task = Task(task_description, False, "", date.today())
        my_task_list.add_task(task)
    # 2. Print Tasks
    elif option == 2:
        my_task_list.print_tasks()
    #Remove a task
    elif option == 3:
        my_task_list.print_tasks()
        bad_task = int(raw_input("To remove a task, type in the number of the task you want to remove."))
        my_task_list.remove_task(bad_task)
    #4. Complete a task
    elif option == 4:
        my_task_list.print_tasks()
        completedtask = int(raw_input("To complete a task, type the number of the task you want to complete."))
        my_task_list.complete_task(completedtask)
    #5: View completed tasks
    elif option == 5:
        my_task_list.print_done_list()
    # 6. Exit:
    #Break exits the while loop
    elif option == 6:
        f = open("tasks.txt", "w")
        for task in my_task_list.not_done:
            f.write(task.get_task_summary() + "\n")
        for task in my_task_list.done:
            f.write(task.get_task_summary() + "\n")
        f.close()
        break
    elif option == 7:
        break
    else:
        print "I don't know."

#Sort by subject
#Sort by date

#HW:
#Codecademy Classes Lesson
#Write comments for all methods + classes explaining what they do

"""
date_instance = date(2017, 1, 3)
synopsis = Task("Read chapters 12-17 ", False, "Math", date_instance)
print synopsis.description
print '%s/%s/%s' % (date_instance.month, date_instance.day, date_instance.year,)

subjects = [Task("English", "Annotate chapter 13", date.today()),
            Task("Math", "Practice problems", date.today()), Task("French", "CVG page 20", date.today())]

homework = TaskList("Read 12 pgs", ())

grocery_list = TaskList()
grocery_list.add_task(Task("orange", False, "food", date(2018, 3, 10)))
grocery_list.add_task(Task("Lettuce", False, "vegetables", date(2017, 3, 6)))
grocery_list.add_task(Task("bread", True, "carbs", date(2017, 2, 27)))
grocery_list.add_task(Task("juice", True, "drinks", date(2018, 3, 10)))




print subjects
print "\nunsorted"
print "date,      task,            subject"
subjects_task_sort = sorted(subjects, key=lambda TaskListElement: TaskListElement.task)
for tl in subjects_task_sort:
    print tl
print "\nsorted on task"
print "subject, task, date"
subjects_date_sort = sorted(subjects, key=lambda TaskListElement: TaskListElement.date)
for tl in subjects_task_sort:
    print tl
"""