#Assign list
to_do_list = []
completed = []

from datetime import date
#^^This imports date from the datetime library
class Task(object):
    """ Holds methods for setting a due date, assigning a subject and synopsis of your task"""
    def __init__(self, description, completed, subject, date):
        """__init__ initializes things so that they can be used in dot notation"""
        self.completed = completed
        self.description = description
        self.subject = subject
        self.date = date
    def is_due(self):
        """This method makes it so that the user can set a due date for their task
        param: none
        :return: if your task is overdue or if you still have time."""
        return date.today() >= self.date
    def task_summary(self):
        """This method prints out a description and summary for your task.
        param: none
        :return: summary and description of task"""
        print self.description
        print self.subject

    def __str__(self):
        return str(self.subject) + ": " + str(self.task) + ", " + str(self.date)


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
        self.not_done.append(new_task)


    def remove_task(self, index):
        """removes tasks from a list
        param: index
        :return: None"""
        removed_task = self.not_done.pop(index)

    def complete_task(self, index):
        """completes a task
        param: index
        :return: None"""
        completed_task = self.not_done[index]
        complete_task.completed = True
        self.not_done.pop(index)
        self.done.append(self.not_done.pop(index))

    def sort_tasks(self, sort_by):
        """Sorts tasks by subject or date
        param: sort_by
        :return: in some cases, 'this isn't supported!'"""
        if sort_by == "subject":
            #TODO: homework March 7
            pass
        elif sort_by == "date":
            #TODO: homework March 7
            pass
        else:
            print "This isn't supported!"

def print_tasks():
    """prints out your task list
    param: none
    :return: prints out your to-do list including its due dates"""
    print to_do_list
    mylist = Task("Walk Leo, Return book, Get groceries, Write card. ")
    print mylist
    print '%s/%s/%s' % (now.month, now.year,)

def add_task():
    """adds your task to your list
            param: none
        :return: prints out yout task"""
    task = raw_input("What is your task? ")
    to_do_list.append(task)
    task = Task("Math HW ")
    print task
    print '%s/%s/%s' % (now.month, now.day, now.year,)

def print_enumerated_tasks():
    """enumerates your tasks and lets your user print
        param: none
        :return: prints enumerated task"""
    for i, task in enumerate(to_do_list):
        print i, task

def complete_task():
    """Completes your task
        param: none
        :return: None"""
    print_enumerated_tasks()
    task_index = int(raw_input("To complete a task, type the number of that task. "))
    task = to_do_list.pop(task_index)
    completed.append(task)

def view_completed():
    """lets you view your completed tasks
            param: none
        :return: prints out your list with completed tasks"""
    print completed

def remove_task():
    """removes a task from your to-do list
        param: none
        :return: none"""
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

#Sort by subject
#Sort by date

#HW:
#Codecademy Classes Lesson
#Write comments for all methods + classes explaining what they do

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
print "subject,      task,            date"
subjects_task_sort = sorted(subjects, key=lambda TaskListElement: TaskListElement.task)
for tl in subjects_task_sort:
    print tl
print "\nsorted on task"
print "subject, task, date"
subjects_date_sort = sorted(subjects, key=lambda TaskListElement: TaskListElement.date)
for tl in subjects_task_sort:
    print tl