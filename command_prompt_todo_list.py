#Assign list
to_do_list = []
completed = []

'''
# Version 1:
number_tasks = int(raw_input("How many tasks do you have?"))

print number_tasks
count=0
#Begin loop
while(count<number_tasks):
    #Ask user for input
    task = raw_input("What is your task?")
    #Add to list
    to_do_list.append(task)
    count= count +1
#Print tasks
print to_do_list


while(0<number_tasks):
    number_tasks= number_tasks -1
    print number_tasks'''

while (True):
    # casting the string input to an integer
    option = int(raw_input("Choose an option:\n"
                           "1. Add a task\n"
                           "2. Print tasks\n"
                           "3. Exit app\n"
                           "4. Complete a task\n"))
    # 1. Add a task
    if option == 1:
        task = raw_input("What is your task?")
        to_do_list.append(task)
    # 2. Print Tasks
    elif option == 2:
        print to_do_list
    # 3. Exit
    elif option == 3:
        break
    #4. Complete a task
    elif option == 4:
        for i, task in enumerate(to_do_list):
            print i, task
        task_index = int(raw_input("To complete a task, type the number of that task. "))
        task = to_do_list.pop(task_index)
        completed.append(task)
    else:
        print "I don't know."

    #Expand selection
    #finish rawinput
    #make function for each

