my_list = []
words = ("add", "delete", "update")
while True:
    user = input("what action do u want \n"
                 "add\n"
                 "delete\n"
                 "update\n"
                 "or (exit) to end ")

    if user.lower() == "exit":
        break

    if user.lower() in words:
        if user.lower() == "add":
            add = input("what task do u want to add?")
            my_list.append(add)
            print("add completed")

        elif user.lower() == "delete":
            print("your current tasks are ", my_list)
            delete = input("what task do u want to delete? ")
            if delete in my_list:
                my_list.remove(delete)
                print("the task deleted ")
            else:
                print("task doesnt exist")

        elif user.lower() == "update":
            if not my_list:
                print("there is no task")
            for count, task in enumerate(my_list, start=1):
                print(count, task)
            index = int(
                input("what is the nuber of the text u want to change?"))-1
            new_task = input("what is the new task?")
            if 0 <= index < len(my_list):
                my_list[index] = new_task
            else:
                print("invalid number")
    else:
        print("please enter a valid input")

    print("your current tasks are ", my_list)


    #later add a gui version with tkinter
    #written by sage 12/12/2025
